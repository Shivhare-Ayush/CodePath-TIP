'''
U - find min element
M- The challenge is a solution which is O(log n) this is now needing a DC algorithm 
P- Since the array was originally in ascending order, we can still apply some search algorithms. 
Divide and conquor is Log N, and we can start from partition, and then create 2 child processes. Each process tries to find.

If left > current or right < current, then that left or right element is minimum. 

I - 
R - 
E - 


'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1
        return nums[left]
                