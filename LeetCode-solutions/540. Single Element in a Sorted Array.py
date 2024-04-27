'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''
def singleNonDuplicate(nums):
        nums.append(-1)
        nums.insert(0,-1)
        for i in range(1,len(nums)-1):
            if nums[i+1]!=nums[i] and nums[i-1]!=nums[i]:
                return nums[i]
print(singleNonDuplicate(nums=[3,3,7,7,10,11,11]))
        