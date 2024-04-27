'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
'''
num=1
list1=[]
if n%2!=0:
    list1.append(0)
    n-=1
for i in range(n):
    if num not in list1:
        list1.append(num)
    elif num in list1:
        list1.append(-num)
    if -num in list1:
        num+=1
return list1