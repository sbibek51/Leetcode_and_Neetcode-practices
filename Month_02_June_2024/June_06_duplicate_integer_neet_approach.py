#Bibek Shiwakoti

'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''


class Solution:
    def has_duplicate(self,nums)->bool:
        hasset= set()

        for n in nums:
            if n in hasset:
                return True
            hasset.add(n)
        return False


obj = Solution()
print(obj.has_duplicate([1,2,3,4,4]))
print(obj.has_duplicate([1,2,3,4]))
