from collections import Counter


# https://leetcode.com/problems/task-scheduler/
class Solution:
    # mathy solution - 70th percentile
    # apparently everything is determined by the "most frequent" task (max count): either it has gaps or it doesn't.
    # if it doesn't, neither will any of the less frequent tasks. I can see this now, but it's still hard to explain.
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_count = len(tasks)
        if not n:
            return task_count

        task_counts = list(Counter(tasks).values())
        max_task_count = max(task_counts)
        max_interval = (max_task_count - 1) * (n + 1) + 1

        # if there are multiple "max intervals", their starts must be staggered
        offset = task_counts.count(max_task_count) - 1  # -1 b/c 1 max -> 0 offset
        total_max_interval = max_interval + offset
        return max(task_count, total_max_interval)  # either no gaps or gaps


    # simulation - VERY SLOW, 10th percentile - but it was kinda fun, so I left it here
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if not n:
            return len(tasks)

        tasks = Counter(tasks)
        cooldowns = {k: 0 for k in tasks.keys()}
        scheduled = []
        i = 0
        while tasks:
            ready = [task for task, cooldown in cooldowns.items() if not cooldown]
            if ready:
                task = max(ready, key=lambda task: tasks[task])
                scheduled += [task]
                count = tasks[task]
                if count > 1:
                    tasks[task] = count - 1
                    cooldowns[task] = n + 1  # +1 b/c cooldown is measured from task end, but this is task start
                else:
                    tasks.pop(task)
                    cooldowns.pop(task)
                for k, v in cooldowns.items():
                    if v:
                        cooldowns[k] = v - 1
                i += 1
            else:
                step = min(cooldowns.values())
                scheduled += [None] * step
                for k, v in cooldowns.items():
                    if v:
                        cooldowns[k] = v - step
                i += step

        return len(scheduled)
