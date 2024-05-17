'''You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 '''

class Solution(object):
    def mySqrt(self, x):
        lower_perfect_sq=1
        lower_root =1
        i=1
        while (lower_perfect_sq<=x):
            lower_perfect_sq = i*i
            lower_root = i
            i+=1

        return lower_root-1

obj = Solution()
print(obj.mySqrt(8))
print(obj.mySqrt(1688))