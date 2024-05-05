'''
You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

 

Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.


'''
def maximumPrimeDifference(nums):
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        out = []
        for i in range(len(nums)):
            if isPrime(nums[i]):
                out.append(i)
        if len(out)>1:
            return out[-1]-out[0]
        else:
            return 0
print(maximumPrimeDifference( nums = [2,2]))