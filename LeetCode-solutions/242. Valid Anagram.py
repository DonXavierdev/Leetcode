'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
if len(s)>len(t) or len(t)<len(s):
    return False
a=list(t)
for i in s:
    if i in a:
        a.remove(i)
if a!=[]:
    return False
return True