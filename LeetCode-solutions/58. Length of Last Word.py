'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''
s = "hi Hello World  "
space=''
l=''
for i in s[::-1]:
    if i==" ":
        space+=i
    else:
        break
for i in s[-(len(space))-1::-1]:
    if i==" ":
        break
    else:
        l+=i
print(len(l))




