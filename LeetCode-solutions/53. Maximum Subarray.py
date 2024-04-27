'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

'''
max_sum = nums[0]
current_sum = nums[0]
for num in nums[1:]:
    current_sum = max(current_sum + num, num)
    max_sum = max(max_sum, current_sum)
    #if num > current_sum + num:
    #    current_sum = num
    #else:
    #    current_sum += num
    #if current_sum > max_sum:
    #    max_sum = current_sum
    #print (num, current_sum, max_sum)
return (max_sum)


