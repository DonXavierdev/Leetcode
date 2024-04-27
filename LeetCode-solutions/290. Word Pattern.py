'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false 
'''
s=s.split()
if len(s)!=len(pattern):
    return False
for i in range(len(s)-1):
    if s[i]==s[i+1] and pattern[i]!=pattern[i+1]:
        return False
list1=[s[0]]
list2=[pattern[0]]
for i in s:
    if i not in list1:
        list1.append(i)
for i in pattern:
    if i not in list2:
        list2.append(i)
if len(list1)==len(list2):
    return True
        