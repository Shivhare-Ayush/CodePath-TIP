'''
Plans - Sort all strings, frequency map for all strings

It will be ALOT of space for the multiple frequency maps. So although sorting will be slower, it will be the cleanest solution 

Now we sort each word, and store that sorted word into a hashmap

U - anagrams must be combined into lists 
M - sorting, lists, hash sets, strings, 
P - hash key can be sorted version of anagrams, and each key has a list value. Then we make a list of the values and return that.
I - 
R - O(n) time and O(n) space scales with anagrams and words 
E - handles len(strs) being 0 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for word in strs:
            sort = sorted(word)
            sort = "".join(sort)
            sorted_words.setdefault(sort, []).append(word)
        return list(sorted_words.values())
        