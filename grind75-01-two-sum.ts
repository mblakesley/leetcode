// https://leetcode.com/problems/two-sum
// O(n) solution using obj's - 80th percentile
function twoSum(nums: number[], target: number): number[] {
    let oldVals = {}  // { oldVal: oldIndex }
    for (let [i, num] of nums.entries()) {
        let complement = target - num
        let oldIndex = oldVals[complement]
        if (oldIndex !== undefined) {
            return [oldIndex, i]
        }
        oldVals[num] = i
    }
    return []
}
