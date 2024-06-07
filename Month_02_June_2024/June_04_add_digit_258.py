#Bibek Shiwakoti
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
'''




class Solution(object):
    def addDigits(self, num):
       while num >9:
            str_num = str(num)
            for i in str_num:
                digit_sum = sum(int(digit) for digit in str_num)
                num = int(digit_sum)
       return num


obj = Solution()
print(obj.addDigits(99))