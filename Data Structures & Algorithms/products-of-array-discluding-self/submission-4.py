'''
U - Create a result array, which contains the products of every element in the array except current one. 
M - prefix sum 
P - First multiply every element together, then divide by nums[i] = result[i]
I
R
E the problem is if there is a zero in the nums, we cannot divide 0 by 0. So instead we calculate the not inclusive prefix sum 
prefix[0] = 1, sufix[0] = 48
prefix[1] = 1, sufix[1] = 24 

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [1] * len(nums)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res





        