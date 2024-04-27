'''Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.'''
# normal iteration method
def maximumcount(nums):
    neg=0
    pos=0
    for i in nums:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1
    return max(pos,neg)
nums = [-3,-2,-1,0,0,1,2]
print(maximumcount(nums))
#second method using lambda to clear out 0's
def maximumCount(nums):
    filnums=list(filter(lambda num: num != 0, nums))
    pos=0
    for i in filnums:
        if i>0:
            pos=filnums.index(i)
            break
    return max(len(filnums[:pos]),len(filnums[pos:]))
nums = [-3,-2,-1,0,0,1,2]
print(maximumCount(nums))
