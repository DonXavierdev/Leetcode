'''
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.

 

Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

 
'''
def findLatestTime(s):
        s= s.split(':')
        Hr = list(s[0])
        Min = list(s[1])
        if Hr[0] == '?':
            if Hr[1] == '?':
                Hr = '11'
            elif int(Hr[1]) > 1 :
                Hr[0] = '0'
            else:
                Hr[0] = '1'
        elif Hr[1] == '?':
            if Hr[0] == '1':
                Hr[1] = '1'
            else:
                Hr[1] = '9'
        if Min[0] == '?':
            if Min[1] == '?':
                Min = '59'
            else:
                Min[0] = '5'
        elif Min[1] == '?':
                Min[1] = '9'
        s =''.join(Hr) + ':' + ''.join(Min)
        return s
print(findLatestTime(s="0?:5?"))