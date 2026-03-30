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
        print(nums)
        n = len(nums)
        prefix = [1, nums[0]]
        for num in nums[1:-1]:
            prefix.append(prefix[-1] * num)

        sufix = [1, nums[-1]]
        nums = nums[:-1]
        for i in range(len(nums)-1, 0, -1):
            print(i)
            print(nums[i])
            sufix.append(sufix[-1] * nums[i])
        result = []
        print(prefix, sufix)
        for i in range(n):
            result.append(prefix[i] * sufix.pop())
        return result




        