'''
Understand- find most frequent element (frequency map)
M - Might be worth trying to sort instead 
P - if 
I - 
R - Create a frequency map, then sort it. Then return the top k [-k:]
E - 
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        
        for key, val in freq.items():
            count[val].append(key)
        print 
        result = []
        for i in range(len(count) -1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result
        