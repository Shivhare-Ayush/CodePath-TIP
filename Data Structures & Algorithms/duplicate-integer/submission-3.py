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
        if len(set(nums)) != len(nums):
            return True
        return False