'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
'''
ans=[]
nums.sort()
if nums[0] < 0 and nums[1] < 0 and nums[-1]>0:
    ans.append(nums[0]*nums[1]*nums[-1])
if nums[0] < 0 and nums[1] < 0 and nums[-1]<0:
    ans.append(nums[-1]*nums[-2]*nums[-3])
else:
    ans.append(nums[-1]*nums[-2]*nums[-3])
return max(ans)