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
        if len(s) != len(t):
            return False 
        counter = {}
        
        for char in s:
            counter[char] = counter.get(char,0) + 1
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        return True
