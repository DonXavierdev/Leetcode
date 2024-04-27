'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
'''
def secondHighest(s):
    list1=[]
    for i in s:
        if i.isdigit():
            list1.append(int(i))
    if list1==[]:
        return -1
    list1=set(list1)
    if len(list1)==1:
        return -1
    else:
        list1.remove(max(list1))
        return max(list1)
s="dfa12321afd"
print(secondHighest(s))
