'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example  1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
a=list(magazine)
list1=[]
for i in ransomNote:
    if i in a:
        list1.append(i)
        a.remove(i)
if list1==list(ransomNote):
    return True
