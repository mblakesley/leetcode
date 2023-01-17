# https://leetcode.com/problems/course-schedule/
class Solution:
    # backtracking (DFS) - 80th percentile
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        self.graph = {}
        for course, prereq in prerequisites:
            courses = self.graph.setdefault(prereq, [])
            courses += [course]

        self.old_paths = set()
        self.current_path = set()
        for prereq in self.graph:
            if not self.process_prereq(prereq):
                return False
        return True

    def process_prereq(self, prereq: int) -> bool:
        self.current_path |= {prereq}
        courses = self.graph.get(prereq, [])
        for course in courses:
            if course in self.old_paths:  # this path has encountered an old path (not a loop)
                continue
            if course in self.current_path:  # this path has encountered itself (loop)
                return False
            if not self.process_prereq(course):  # check subsequent nodes
                return False
        self.current_path -= {prereq}
        self.old_paths |= {prereq}
        return True
