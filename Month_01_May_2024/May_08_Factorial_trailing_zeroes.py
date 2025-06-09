#Bibek Shiwakoti
'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0

'''


#Attempt 1:
'''class Solution(object):
    def trailingZeroes(self, n):

        if n<=0:
            return 0
        else:
            factorial = 1
            while n>0:
                factorial = factorial * n
                n = n-1

            count_of_zeroes = 0
            while factorial >0:
                if factorial% 10 == 0:
                    count_of_zeroes=count_of_zeroes+1
                else:
                    break
                factorial=factorial//10



            return count_of_zeroes
This code does worked but the thing is it is taking a longer time so need to try some optimize code
'''


class Solution(object):
    def trailingZeroes(self, n):

        if n <= 0:
            return 0
        else:

            count_of_zeroes = 0
            while n >= 5:
                count_of_zeroes = count_of_zeroes + n // 5
                n = n // 5

            return count_of_zeroes


obj = Solution()
print(obj.trailingZeroes(5))
print(obj.trailingZeroes(3))



