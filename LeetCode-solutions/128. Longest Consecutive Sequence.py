'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
'''
def longestConsecutive(nums):
        nums = set(nums)
        start = 0
        length = 0
        max_length = 0
        for i in nums:
            if i-1 not in nums:
                start = i
                while start+1 in nums:
                    length += 1
                    start += 1
                length += 1
                max_length = max(max_length,length)
                length = 0
        return max_length
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))