'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.


'''

strs = ['flower', 'flow', 'flht']
# strs = ['f', 'fl', 'fl']
index = 0
res=''
flag=True
if len(strs)==1:
    print(strs[0])
while flag==True:
    for i in range(len(strs)-1):
        if index>=len(strs[i]) or  index>=len(strs[i+1]):
            flag=False
            break    
        if strs[i][index]!=strs[i+1][index]:
            flag=False
        else:
            continue
    if flag!=False:
        res+=strs[i][index]
    index+=1
print(res)






    