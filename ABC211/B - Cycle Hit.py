s = []
for i in range(4):
  s.append(input())
set_s = set(s)
if("H" in set_s and "2B" in set_s and "3B" in set_s and "HR" in set_s):print("Yes")
else:print("No")
