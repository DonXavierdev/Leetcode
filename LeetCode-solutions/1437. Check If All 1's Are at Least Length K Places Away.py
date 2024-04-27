'''
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:


Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:


Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
'''
def kLengthApart(nums,k):
    Have_seen_1 = 0
    gap = 0
    for i in range(len(nums)):
        if nums[i]==0:
            gap+=1
        elif nums[i]==1 and Have_seen_1==0:
            Have_seen_1=1
        elif nums[i]==1 and Have_seen_1==1:
            if gap<k:
                return False
            gap=0
    return True
print(kLengthApart([1,0,0,0,1,0,0,1],2))