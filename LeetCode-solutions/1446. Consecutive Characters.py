'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
'''
s+='&'
if len(s)==1:
    return 1
nums=[]
index=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        index+=1
    else:
        nums.append(index)
        index=0
return max(nums)+1