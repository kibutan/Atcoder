list = ["0","1","2","3","4","5","6","7","8","9"]
s = str(input())
temp =[]
for i in range(len(s)):
  temp.append(s[i])
print(*(set(temp) ^ set(list)))
