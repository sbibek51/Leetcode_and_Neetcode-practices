#Bibek Shiwakoti

'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

'''


class Solution (object):
    def longer_pallindrome(self,s):
        d = {}
        for i in s:
         d[i] = d.get(i,0)+1

        length = 0
        flag = False

        for count in d.values():
            if count % 2 == 0:
                length  = length +count
            else:
                length = length + (count-1)
                flag = True # to check if there is odd length string or not


        if flag:
            return length+1
        else:
            return length




obj = Solution()
s= 'abccccdd'
print(obj.longer_pallindrome(s))

s= 'b'
print(obj.longer_pallindrome(s))