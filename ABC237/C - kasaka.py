from itertools import groupby
s = input()
ans ="No"
if len(set(s)) == 1:
    print("Yes")
    exit()

word_group = list([(k,list(g)) for k,g in groupby(s)])
a_start = [word_group[0][1] if word_group[0][0] == "a" else ""]
a_end = [word_group[-1][1] if word_group[-1][0] == "a" else ""]
if(len(*a_start) > len(*a_end)):
    print("No")
    exit()

t = s.strip("a")

i = 0
if(False if i < 0 else t == t[::-1]):print("Yes")
else:print("No")
