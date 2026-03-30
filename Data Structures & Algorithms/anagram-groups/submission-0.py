'''
Plans - Sort all strings, frequency map for all strings

It will be ALOT of space for the multiple frequency maps. So although sorting will be slower, it will be the cleanest solution 

Now we sort each word, and store that sorted word into a hashmap
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for word in strs:
            sort = sorted(word)
            sort = "".join(sort)
            if sort in sorted_words:
                sorted_words[sort].append(word) 
            else:
                sorted_words[sort] = [word]
        print(sorted_words.values())
        result = []
        for arr in sorted_words.values():
            result.append(arr)
        return result
        