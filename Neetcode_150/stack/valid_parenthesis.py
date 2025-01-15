# 1/15/2025
# Bibek Shiwakoti
# Valid parenthes

'''
Valid Parentheses
Solved
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

obj = Solution()

def call_me(s):
    if(obj.isValid(s)):
        print('given parenthes',s, 'is valid')
    else:
        print('given parenthes',s, 'is not valid')

s = "([{}])"
call_me(s)

s = "([{}])}"
call_me(s)


#alternative way
'''
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == '''''