#Bibek Shiwakoti
#Jan 3 , 2025

'''
Encode and Decode Strings
Solved
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

'''



class Solution:

    def encode(self, strs: list[str]) -> str:
        result =''
        for s in strs:
            result +=str(len(s))+'#'+s
        return result

    def decode(self, s: str) -> list[str]:
        result_decode,i = [],0

        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            result_decode.append(s[j+1:j+1+length])
            i= j+1+length
        return result_decode



obj = Solution()
print(obj.encode(["neet","code","love","you"]))
print(obj.decode(obj.encode(["neet","code","love","you"])))