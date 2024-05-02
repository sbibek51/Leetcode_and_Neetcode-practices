'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false


Constraints:

-231 <= n <= 231 - 1

'''


"""if number n is power of two then its ANDING with n-1 is zero because there is only
 one bit is 1 eg: for 8 binary is : 1000"""

class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        else:
            return (n & (n-1)) ==0


obj = Solution()
print(obj.isPowerOfTwo(1))
print(obj.isPowerOfTwo(2))
print(obj.isPowerOfTwo(4))
print(obj.isPowerOfTwo(15))
print(obj.isPowerOfTwo(16))