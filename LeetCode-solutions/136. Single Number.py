'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

'''
nums.sort()
if len(nums)==1:
    return nums[0]
if nums[0]!=nums[1]:
    return nums[0]
if nums[-1]!=nums[-2]:
    return nums[-1]
for i in range(1,len(nums)):
    if nums[i-1]!=nums[i] and nums[i+1]!=nums[i]:
        return nums[i]
    