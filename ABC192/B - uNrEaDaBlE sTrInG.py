s = input()
if(len(s) == 1):
  if(s.islower()):
    print("Yes")
    exit()
  else:
    print("No")
    exit()
 
if(s[0::2].islower()):
#  print(s[0::2].islower())
#  print(s[0::2])
  if(s[1::2].isupper()):
#    print(s[1::2])
    print("Yes")
    exit()
print("No")
