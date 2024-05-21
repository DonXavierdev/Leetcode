s = "aaaaebbbbcccc"
dict_s = {}
for i in s:
    if i in dict_s:
        dict_s[i] +=1
    else:
        dict_s[i] = 1
print(dict_s)