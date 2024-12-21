#Bibek Shiwakoti
#Neetcode practice question

'''
    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''

class Solution:
    def twoSum(self,nums:list[int],target:int)->list[int]:
        hashPrev={} # to create a hashmap of all elements
        for i,n in enumerate(nums):
            diff = target-n # calculating diff and will look if diff is in our hashmap
            if diff in hashPrev:
                return [hashPrev[diff],i]  #returning index of diff and current num
            hashPrev[n]=i
        return # though return is already done



obj = Solution()
print(obj.twoSum([1,2,3,4],7)) #output expected: 2,3