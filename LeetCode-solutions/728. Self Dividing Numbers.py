'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]
'''
def selfDividingNumbers(left,right):
    out=[]
    for i in range(left,right+1):
        flag=0
        for j in str(i):
            if j=='0':
                flag=1
                break
            if i%int(j)!=0:
                flag=1
                break
        if flag==0:
            out.append(i)
    return out
print(selfDividingNumbers(left=1,right=22))