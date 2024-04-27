'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''
list1=[]
list2=[]
add=1
summ=0
for i in num1:
    list1.append(i)
for i in num2:
    list2.append(i)
for i in list1[::-1]:
    i=int(i)
    i*=add
    summ+=i
    add*=10
add=1
for i in list2[::-1]:
    i=int(i)
    i*=add
    summ+=i
    add*=10
return str(summ)
    