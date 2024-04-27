'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''
a=list(s)
p=''
for i in s:
    a.remove(i)
    if i in a:
        a.append(i)
    else:
        p+=i
        return s.index(p)
return -1