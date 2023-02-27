import re
s= input()
for i in range(len(s)):
  if(re.search("[A-Z]",s[i])):print(i+1)
