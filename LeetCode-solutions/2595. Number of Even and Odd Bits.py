'''
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].

 

Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
It contains 1 on the 0th and 4th indices. 
There are 2 even and 0 odd indices.
Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index. 
There are 0 even and 1 odd indices.
'''
def evenOddBit(n):
    temp=str(bin(n)[2:])[::-1]
    odd=0
    even=0
    for i in range(len(temp)):
        if int(temp[i])==1 and i%2==0:
            even+=1
        elif int(temp[i])==1 and i%2!=0:
            odd+=1
    return [even,odd]
n=17
print(evenOddBit(n))