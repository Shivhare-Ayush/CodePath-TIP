'''
Understand - like HTTPS, we create a concatenation function, which also provides intructions on how to break it back apart 
Match - 
Plan - 
I
R
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            n = len(string)
            result += str(n) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        num = ''
        integer = -1
        i = 0
        while i < len(s):
            print('i', i)
            if s[i] == '#':
                #num is found
                integer = int(num)
                num = ''
            else:
                num += s[i]

            if integer > -1: 
                word = s[i+1:i+1+integer]
                print(word)
                result.append(word)
                i += integer
            integer = -1
            i += 1

        return result
