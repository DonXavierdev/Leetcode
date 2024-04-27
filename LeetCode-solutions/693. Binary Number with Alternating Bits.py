'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
'''
def hasAlternatingBits(n):
        a=bin(n)[2:]
        res=''
        flag=0
        for i in range(len(a)):
            if flag==0:
                res+='1'
                flag=1
            else:
                res+='0'
                flag=0
        return a==res
print(hasAlternatingBits(5))