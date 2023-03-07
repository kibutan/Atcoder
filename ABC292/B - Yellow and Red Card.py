n,q= list(map(int,input().split()))
event=[list(map(int,input().split())) for _ in range(q)]
card = [0] * (n+1)
#print(event)
for i in range(q):
  #print("i",i)
  if(event[i][0] == 1):
      card[event[i][1]] += 1
  if(event[i][0] == 2):
      card[event[i][1]] += 2
  if(event[i][0] == 3):
      print("Yes") if card[event[i][1]] >= 2 else print("No")
  
