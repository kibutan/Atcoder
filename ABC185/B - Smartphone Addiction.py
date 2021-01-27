#n[mAh], M times visit to cafes, at home @ T
n,m,t = list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(m)]

bat = n
time = 0

print(ab)
for i in range(len(ab)):
  bat -= int(ab[i][0] - time)
  if(bat <= 0):
    print("No")
    exit()
  print("-bat",int(ab[i][0] - (time)))
  bat += int(ab[i][1] - ab[i][0])
  if(bat >= n):bat = n
  print("+bat",int(ab[i][1] - ab[i][0]))
  print(bat)
  time = ab[i][1]
bat -= int(t - time)
print("home",bat)
if(bat > 0):print("Yes")
else:print("No")
