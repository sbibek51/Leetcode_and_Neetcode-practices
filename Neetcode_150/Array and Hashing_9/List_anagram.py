#Bibek Shiwakoti
#Jan 1st 2025

#question:

'''
    Group Anagrams
Solved
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''

from collections import defaultdict
#the defaultdict class is not directly built into Python. we need to explicitly import it from the collections module
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0]*26 #q ...z
            for c in s: #going thru each char in string
                count[ord(c)-ord('a')] +=1
            result[tuple(count)].append(s) #list cant be key so using tuple
        return result.values()


obj = Solution()
print(obj.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(obj.groupAnagrams(["ab","ba","aabb","cat","stop","hat",'pots']))