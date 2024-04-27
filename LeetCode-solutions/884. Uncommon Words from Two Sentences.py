'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
'''
def uncommonFromSentences(s1,s2):
        s1=s1.split()
        s2=s2.split()
        s1.extend(s2)
        out=[]
        for i in s1:
            if s1.count(i)==1:
                out.append(i)
        return out
print(uncommonFromSentences(s1="this apple is sweet",s2="this apple is sour"))