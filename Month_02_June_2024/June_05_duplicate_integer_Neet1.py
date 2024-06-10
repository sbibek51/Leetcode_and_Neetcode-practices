#Bibek Shiwakoti

class Solution:
    def hasDuplicate(self, nums) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        non_single_value = [value for key, value in d.items() if value > 1]

        print(non_single_value)



obj = Solution()
obj.hasDuplicate([1,2,3,4,4])