'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
def findNthDigit(n):
        # if n < 9: return n
        digits = 1
        mul = 1
        while (n - (9 * mul * digits)) >= 0:
            n -= (9 * mul * digits)
            digits += 1
            mul *= 10
        if n == 0:
            return int(str(mul-1)[-1])
        number = mul + n//digits - 1
        if n % digits:
            return int(str(number+1)[(n%digits)-1])
        else:
            return int(str(number)[-1])
        return 0
print(findNthDigit(n=12349))