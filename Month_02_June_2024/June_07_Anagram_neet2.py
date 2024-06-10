#Bibek Shiwakoti
'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []

        for char in s:
            list1.append(char)

        for char in t:
            list2.append(char)

        list1.sort()
        list2.sort()



        if list1==list2:
            return True
        else:
            return False
s= 'jar'
t= 'jam'

s1= 'jar'
t1= 'raj'

obj = Solution()
print(obj.isAnagram(s,t))
print(obj.isAnagram(s1,t1))