'''
UMPIRE method 
Understand - We check for any repeating element
Match patterns - Array, (set for no duplicates)
Plan your approach - get the length of array, check for each element, is there another element ==. 
Implement 
Runtime (time complexity) - How can I speed it up or improve space/time
E edge cases 
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True

        return False 