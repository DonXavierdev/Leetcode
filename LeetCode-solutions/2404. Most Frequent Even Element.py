'''
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

'''
nums =[8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
temp=[]
for i in nums:
    if i%2==0 and temp==[]:
        temp.append(i)
    elif i%2==0 and nums.count(i)>nums.count(temp[0]):
        temp.append(i)
        temp.remove(temp[0])
    elif i%2==0 and nums.count(i)==nums.count(temp[0]):
                if i<temp[0]:
                    temp.append(i)
                    temp.remove(temp[0])
if temp==[]:
    print(-1)
else:
    print(min(temp))