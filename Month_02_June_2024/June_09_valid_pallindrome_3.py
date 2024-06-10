#Bibek Shiwakoti
'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str = s.lower()
        my_list = []


        my_list =''.join(char for char in my_str if char.isalnum())
        return my_list == my_list[::-1]


obj = Solution()
print(obj.isPalindrome('bibek'))


