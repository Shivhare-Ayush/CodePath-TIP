'''
U - we return boolean based on checking if two strings have same charecters
M - frequency map for both strings and then check if its equal. 
P - Create a 
I - 
R - Best run time because sorting would be NlogN and frequency map is N. 
E -  None 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = {}
        freq_map_t = {}
        for char in s:
            if char in freq_map_s:
                freq_map_s[char] += 1
            else:
                freq_map_s[char] = 1
        for char in t:
            if char in freq_map_t:
                freq_map_t[char] += 1
            else:
                freq_map_t[char] = 1
        if freq_map_t == freq_map_s:
            return True
        return False
