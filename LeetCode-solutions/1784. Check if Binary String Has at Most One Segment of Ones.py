'''
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 
'''
def checkOnesSegment(s):
        s+='9'
        flag=0
        for i in range(len(s)-1):
            if s[i]=='1' and flag==1:
                return False
            if s[i]=='1' and s[i+1]=='0':
                flag=1
        return True
print(checkOnesSegment(s='1001'))