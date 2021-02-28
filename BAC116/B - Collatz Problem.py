s = int(input())
list = []
list.append(s)
i = 0
while True:
  i += 1
#  print("list",list)
  if(s % 2 == 0):
    s = int(s/2)
    if(s in list):
      print(i+1)
      exit()
    else:
      list.append(s)
  else:
    s = 3*s+1
    if(s in list):
      print(i+1)
      exit()
    list.append(s)
