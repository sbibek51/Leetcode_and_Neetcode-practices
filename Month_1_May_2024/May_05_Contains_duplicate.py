#Bibek Shiwakoti
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution(object):
    def containsDuplicate(self, nums):
        l1 = len(nums)
        l2 = len(set(nums))
        return l1!=l2


obj = Solution()
nums_list_1 = [1,1,1,3,3,4,3,2,4,2]
nums_list_2 = [1,2,3,4]
print(obj.containsDuplicate(nums_list_1))
print(obj.containsDuplicate(nums_list_2))