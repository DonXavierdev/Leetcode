'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


'''
s = "(){}[]"
valid={'(':')','[':']','{':'}'}
opening=['(','[','{']
closing=[')',']','}']
summ=0
if len(s)>=4: 
    if s[0] in opening and s[1] in opening and s[-1]!=valid[s[0]] and s[-2]!=valid[s[1]]:
        print(False)
if s[0] in closing or s[-1] in opening:
    print(False)
for i in s:
    if i==opening[0]:
        summ+=1
    if i==opening[1]:
        summ+=2
    if i==closing[0]:
        summ-=1
    if i==closing[1]:
        summ-=2
if summ!=0:
    print(False)
for i in range(len(s)-1):
    if s[i] in opening:
        if s[i+1]!=valid[s[i]] and s[i+1] not in opening:
            print(False)
print(True)



            























