'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
'''
def isMonotonic(nums):
        flag=-1
        if len(nums)<=2:
            return True
        if nums[0]>nums[1]:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
        elif nums[0]==nums[1]:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    flag=1
                    break
                elif nums[i]>nums[i+1]:
                    flag=0
                    break
            if flag==0:
                for i in range(len(nums)-1):
                    if nums[i]<nums[i+1]:
                        return False
            else:
                for i in range(len(nums)-1):
                    if nums[i]>nums[i+1]:
                        return False
        else:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
        return True
print(isMonotonic( nums = [1,3,2]))