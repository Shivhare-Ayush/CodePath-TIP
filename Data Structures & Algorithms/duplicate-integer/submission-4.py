'''
UMPIRE method 
Understand - We check for any repeating element
Match patterns - Array, (set for no duplicates)
Plan your approach - get the length of array, check for each element, is there another element ==. 
Implement 
Runtime (time complexity) - How can I speed it up or improve space/time Use set for O(n) from O(n^2)
E edge cases 
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            dic[num] = num
        return False