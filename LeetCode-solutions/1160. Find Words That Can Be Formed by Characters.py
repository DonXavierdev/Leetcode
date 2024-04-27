'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
out=0
cha=list(chars)
for i in words:
    cha=list(chars)
    out+=len(i)
    for j in i:
        if j in cha:
            cha.remove(j)
        elif j not in cha:
            out-=len(i)
            break
print(out)