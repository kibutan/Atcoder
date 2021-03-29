n = int(input())
a = list(map(int,input().split()))
ans = float('inf')

for bit in range(1 << n):
  bit_list = []
  bad_list = []
 # print("<<",1 << n)
#  print("bit",bit,bin(bit))
  for i in range(n):
    if bit & (1 << i):
#      print("bit:",bit," bit1<<1:",1 << i)
      bad_list.append(a[i])
      bit_list.append(bad_list)
      bad_list = []
    else:
      bad_list.append(a[i])
  if len(bad_list) >=1:bit_list.append(bad_list)
#  print("bit_list",bit_list)
#  print("bad_list",bad_list)
  
  ORs = []
  for i in bit_list:
    or_A = 0
    for j in i:
      or_A |= j
    ORs.append(or_A)
  xor=0
  for i in ORs:
    xor ^= i
  ans = min(ans, xor)
#  print("xor",xor)
print(ans)

  
