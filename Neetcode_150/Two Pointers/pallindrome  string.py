#Bibek Shiwakoti
#1/7/2025

'''
Valid Palindrome
Solved
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
'''

class Solution:
    def isPallindrome(self,s:str)->bool:
        s1=''
        for c in s:
            if c.isalnum():
                s1+=c.lower()
        return s1==s1[::-1]


obj = Solution()
print(obj.isPallindrome('bibek shi'))
print(obj.isPallindrome('Was it a car or a cat I saw'))
print(obj.isPallindrome('tab a cat'))
