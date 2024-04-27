'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0'''
if num<10:
    return num
list1=[]
while num>9:
    list1=[]
    for i in str(num):
        list1.append(int(i))
    num=sum(list1)
return sum(list1)