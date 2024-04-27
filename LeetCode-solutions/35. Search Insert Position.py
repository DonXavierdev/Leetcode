'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

'''
nums=[5,6,7]
target=7
for i in nums:
    if target in nums:
        print(nums.index(target))
        break
    if target>max(nums):
        print(len(nums))
        break
    if target<min(nums):
        print(0)
        break
    if target<i:
        print(nums.index(i))
        break


