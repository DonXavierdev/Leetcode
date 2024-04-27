'''
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
'''
def stringMatching(words):
    out=[]
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] in words[j]: 
                out.append(words[i])
            if words[j] in words[i]:
                out.append(words[j])
    return list(set(out))
words = ["leetcode","et","code"]
print(stringMatching(words))