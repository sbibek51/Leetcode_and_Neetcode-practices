# Bibek Shiwakoti
# 1/10/2025
# Tapping most water

'''
Container With Most Water
Solved
You are given an integer array heights where heights[i] represents the height of the
i
t
h
i
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
'''


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        result = 0
        l,r = 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            result = max(result,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result


obj = Solution()
print('Max area of water is:',obj.maxArea([1,7,2,5,4,7,3,6]))
print('Max area of water is:',obj.maxArea([2,2,2]))