#1/9/2025
# Bibek Shiwakoti

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.
'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for index, val in enumerate(nums):
            if index>0 and val == nums[index-1]:
                continue
            l,r = index+1, len(nums)-1
            while l<r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum <0:
                    l +=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l<r:
                        l += 1
        return res

obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))