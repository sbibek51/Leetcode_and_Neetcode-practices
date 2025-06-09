#Bibek Shiwakoti

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''


class Solution(object):
    def searchInsert(self, nums, target):
        # we can solve using binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # if target not found left is insertion position


obj = Solution()
nums = [1,3,5,6]
target = 5
print(obj.searchInsert(nums,target))

nums1 = [1,3,5,9]
target1 = 7
print(obj.searchInsert(nums1,target1))
