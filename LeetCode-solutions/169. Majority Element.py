'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
'''
nums.sort()
nums.append(1038)
res=0
resc=[]
list1=[nums[0]]
list2=[nums[0]]
for i in nums:
    if i==list1[0]:
        res+=1
    if i!=list1[0]:
        list1[0]=i
        list2.append(i)
        resc.append(res)
        res=1
return list2[resc.index(max(resc))]