#Bibek Shiwakoti
'''
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution(object):
    def isPalindrome(self, x):
        num = x
        num1 = num
        rev_num = 0
        while num > 0:
            rev_num = (rev_num * 10) + num % 10
            num = num // 10
        return rev_num == num1

obj = Solution()
num1=123
num2=121
print(obj.isPalindrome(num1))
print(obj.isPalindrome(num2))