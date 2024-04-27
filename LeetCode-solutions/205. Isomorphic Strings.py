'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''   
if len(set(s))!=len(set(t)):
    return False
list1=[]
list2=[]
for i in range(len(s)):
    if s[i] not in list1 or list1==[]:
        list1.append(s[i])
        list2.append(t[i])
    elif s[i] in list1:
        list2.append(t[list1.index(s[i])])
        list1.append(s[i])
if list2==list(t):
    return True