#Bibek Shiwakoti

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            strs.sort()
            prefix = strs[0]
            for i in range(1, len(strs)):
                for j in range(len(prefix)):
                    if prefix[j] != strs[i][j]:
                        prefix = prefix[:j]
                        break
            return prefix

obj =Solution()
strs =["flower","flow","flight"]
strs1 =["flower","flow","dog"]
print(obj.longestCommonPrefix(strs))
print(obj.longestCommonPrefix(strs1))