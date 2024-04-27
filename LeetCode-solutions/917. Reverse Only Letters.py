'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

'''
list1=[]
res=''
for i in range(len(s)-1,0,-1):
    if s[i].isalpha():
        list1.append(s[i])
if s[0].isalpha():
    list1.append(s[0])
index=0
for i in s:
    if i.isalpha()==False:
        list1.insert(index,i)
    index+=1
for i in list1:
    res+=i
return res