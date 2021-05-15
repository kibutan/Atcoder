s = input()
if(s.count("o") >= 5):
  print(0)
  exit
cnt = 0
valid = []
for i in range(9999):
  pwd = str(0)*(4-len(str(i)))+str(i)
  flag = 0
  valid = []
#  print("pwd",pwd)
  for i in range(4):
    valid.append(s[int(pwd[i])])
    if(s[int(pwd[i])] == "o"):
#      print("o")
      continue
    elif(s[int(pwd[i])] == "?"):
#      print("?")
      flag = 1
    elif(s[int(pwd[i])] == "x"):
#      print("x")
      break
#    print(s[int(pwd[i])])
#  print(valid)
  if(valid.count("o") == s.count("o") and not("x" in valid)):
    print(pwd,valid,"cnt+1")
    cnt += 1
print(cnt)
