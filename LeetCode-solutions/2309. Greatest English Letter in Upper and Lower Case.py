'''
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

 

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.
'''
def greatestLetter(s):
        temp=[]
        maxx=0
        for i in s:
            if i.upper() in s and i.lower() in s:
                temp.append(i)
        for i in temp:
            if ord(i)>maxx:
                maxx=ord(i)
        if maxx==0:
            return ""
        return chr(maxx).upper()
s = "arRAzFif"
print(greatestLetter(s))