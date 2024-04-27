'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
'''
index=0
for i in word:
    if i.islower():
        index+=1
    if len(word)==index:
        return True
index=0
for i in word:
    if i.isupper():
        index+=1
    if len(word)==index:
        return True
index=1
if word[0].isupper():
    word=word[1:]
    for i in word:
        if i.isupper():
            index+=1
    if index==1:
        return True