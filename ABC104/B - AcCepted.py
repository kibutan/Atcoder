import re
s = input()
ans = "AC"
if(s[0] != "A"):ans ="WA"
if(s.count("C") != 1):ans = "WA"
if(s[0] =="C" or s[1] == "C" or s[-1] =="C"):ans ="WA"

for i in range(len(s)):
  if(i == 0 and s[i] == "A"):
#    print("A")
    continue
  elif(i >= 2 and i <= len(s)-2 )and s[i] == "C":
#    print("C")
    continue
  elif(i !=0)and(re.match("[a-z]{1}",s[i])):
#    print("else",s[i],re.match("[a-z]{1}",s[i]))
    continue
  else:
    print(ans,s[i])
    exit()
print(ans)
