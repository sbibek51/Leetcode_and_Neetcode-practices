#Bibek Shiwakoti
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''


class Solution(object):
    def reverse(self, x):
        flag = False
        reverse_digit = 0
        if x < 0:
            flag = True
            x = -x
        while x > 0:
            digit = x % 10
            reverse_digit = reverse_digit * 10 + digit
            x = x // 10

        if (reverse_digit < -2 ** 31 or reverse_digit > 2 ** 31):
            return 0
        else:
            if flag:
                return reverse_digit * (-1)
            else:
                return reverse_digit

obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-159))