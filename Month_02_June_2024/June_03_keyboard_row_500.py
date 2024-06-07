#Bibek Shiwakoti
'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".



Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

'''


class Solution(object):
    def findWords(self, words):
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        result = []

        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)

        return result


obj = Solution()
print(obj.findWords(['bibek', 'dad', 'alaska']))