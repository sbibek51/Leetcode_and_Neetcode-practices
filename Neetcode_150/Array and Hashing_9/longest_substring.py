#Bibek Shiwakoti
#1/6/2025

class Solution:
        def longestConsecutive(self, nums: list[int]) -> int:
            numsSet = set(nums)
            longest = 0

            for n in nums:
                # check if its the start of a sequence
                if (n - 1) not in numsSet:
                    length = 0
                    while (n + length) in numsSet:
                        length += 1
                    longest = max(length, longest)
            return longest


obj = Solution()
print(obj.longestConsecutive([15,14,13,11,-1,0,1,2,19,18,17,16,]))



