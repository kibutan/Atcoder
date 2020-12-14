import re
S = input()
ans = 0
t = ""
for i in S:
  t += i
  if(re.findall('A|G|T|C',t[-1])):continue
  else: 
    ans = max(ans,len(t)-1)
    t = ""
print(max(ans,len(t)))
