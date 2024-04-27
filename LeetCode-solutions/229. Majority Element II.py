'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 
'''
list1=[]
nums2=set(nums)
for i in nums2:
    if nums.count(i)>len(nums)//3:
        list1.append(i)
return list1