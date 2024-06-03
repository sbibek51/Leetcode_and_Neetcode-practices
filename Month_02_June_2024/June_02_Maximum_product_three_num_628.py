#Bibek Shiwakoti
'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6

'''


class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        return max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])
    #after sorting max is either three max or product of negative two lower or max one


obj = Solution()
print(obj.maximumProduct([1,2,3,4]))