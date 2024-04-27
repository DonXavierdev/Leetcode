'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''
def reverseVowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    s=list(s)
    reorder=[]
    for i in range(len(s)):
        if s[i] in vowels:
            reorder.append(s[i])
            s[i]='_'
    reorder=reorder[::-1]
    for i in range(len(s)):
        if s[i]=='_':
            s[i]=reorder[0]
            reorder=reorder[1:]
    res=''
    for i in s:
        res+=i
    return res
print(reverseVowels("leetcode"))
