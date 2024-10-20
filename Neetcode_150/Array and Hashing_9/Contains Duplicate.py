'''

Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false.

'''

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in nums:
                return True
            hashset.add(n)
        return False



obj = Solution()
print(obj.hasDuplicate([1,2,3,4,4]))