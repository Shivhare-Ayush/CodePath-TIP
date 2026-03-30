class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter_parts = {} 
        for i in range(len(nums)):
            num = nums[i]
            if num in counter_parts:
                return [counter_parts[num], i]
            counter_parts[target - num] = i
        return -1

        