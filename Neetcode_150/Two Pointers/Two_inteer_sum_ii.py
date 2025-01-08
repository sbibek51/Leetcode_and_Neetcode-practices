#Bibek Shiwakoti
#1/8/2025

#two integer sum II

'''
Two Integer Sum II
Solved
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashSet = {}

        for i,n in enumerate(numbers):
            diff = target-n
            if diff in hashSet:
               return [hashSet[diff]+1,i+1]
            hashSet[n]=i
        return

obj =Solution()
print(obj.twoSum([1,2,3,4],7))
print(obj.twoSum([1,2,3,4],3))