// Package twosum https://leetcode.com/problems/two-sum
package twosum

// O(n) solution using maps - 70th percentile
func twoSum(nums []int, target int) []int {
	oldVals := map[int]int{} // { oldVal: oldIndex }
	for i, num := range nums {
		complement := target - num
		oldIndex, ok := oldVals[complement]
		if ok {
			return []int{i, oldIndex}
		}
		oldVals[num] = i
	}
	return []int{}
}
