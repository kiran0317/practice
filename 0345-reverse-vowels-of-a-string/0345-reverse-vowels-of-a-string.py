class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A','e','I','o','U','a','E','i','O','u'}
        start = 0
        end = len(s)-1
        s = list(s)
        while start < end:
            first = s[start]
            last = s[end]
            # print(first, last, "first last")
            if (first in vowels) and (last in vowels):
                temp = s[end]
                s[end] = s[start]
                s[start] = temp
                # print(s)
                start +=1
                end-=1
            elif first in vowels:
                end-=1
            else:
                start+=1
        return ''.join(s)