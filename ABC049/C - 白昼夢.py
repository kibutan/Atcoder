S = input()
S_inv = S[::-1]
devide = ["dream","dreamer","erase","eraser"]
devide_inv = [0]*4
#print(S_inv)
for i in range(len(devide)):
  devide_inv[i] = devide[i][::-1]
#print(devide_inv)
ans = "NO"
flag = 0
while(flag == 0):
  i = 0
#  print("s_inv:"+S_inv)
  for i in range(len(devide)):
#    print("i"+str(i))
#    print("str[i]"+str(devide[i]))
#    print(S_inv)
    if(S_inv.startswith(str(devide_inv[i]))):
      flag = 0
      S_inv = S_inv[len(devide_inv[i])::]
#      print("s_inv:"+S_inv)
      if(S_inv == ""):
        ans = "YES"
      break
    else:flag = 1
print(ans)
