'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
'''
count=0
mul=1
for i in range(2,n+1):
    mul*=i
for i in str(mul)[::-1]:
    if i=='0':
        count+=1
    else:
        break
return count
    