'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
'''
nums.append(0)
list1=[]
index=0
for i in nums:
    if i==1:
        index+=1
    if i==0:
        list1.append(index)
        index=0
return max(list1)