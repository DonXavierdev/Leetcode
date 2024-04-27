'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
'''
s = "book"
vowels=['a','e','i','o','u']
count=0
count2=0
for i in s[:len(s)//2]:
    if i in vowels or i.lower() in vowels:
        count+=1
for i in s[len(s)//2:]:
    if i in vowels or i.lower() in vowels:
        count2+=1

print(True if count==count2 else False)