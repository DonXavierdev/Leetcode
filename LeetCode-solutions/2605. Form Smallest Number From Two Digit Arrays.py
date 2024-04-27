'''
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
 

Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
'''
def minNumber(nums1,nums2):
        for i in sorted(nums1):
            if i in nums2:
                return i
        if min(nums1)>min(nums2):
            return int(str(min(nums2))+str(min(nums1)))
        else:
            return int(str(min(nums1))+str(min(nums2)))
print(minNumber(nums1=[3,5,2,6],nums2=[3,1,7]))