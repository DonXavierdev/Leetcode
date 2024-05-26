'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
'''
def findWords(words):
        row1=list("qwertyuiop")
        row2=list("asdfghjkl")
        row3=list("zxcvbnm")
        res = []
        curr_row = 'not taken'
        flag = 0
        for i in words:
            for j in i:
                if j.lower() in row1 :
                    if curr_row == 'taken by row1' or curr_row == 'not taken':
                        curr_row = 'taken by row1'
                    else:
                        flag = 1
                        break
                elif j.lower() in row2 :
                    if curr_row == 'taken by row2' or curr_row == 'not taken':
                        curr_row = 'taken by row2'
                    else:
                        flag = 1
                        break
                else:
                    if curr_row == 'taken by row3' or curr_row == 'not taken':
                        curr_row = 'taken by row3'
                    else:
                        flag = 1
                        break
            curr_row = "not taken"
            if flag == 0:
                res.append(i)
            flag = 0
        return res
print(findWords(["Hello","Alaska","Dad","Peace"]))