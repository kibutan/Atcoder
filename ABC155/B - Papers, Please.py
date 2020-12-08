N = int(input())
A = list(map(int, input().split()))
for i in A:
  if(i % 2 ==0):
    if(i % 3 ==0 or i % 5 ==0):ans = 1
    else:
      ans = 0
      print("DENIED")
      exit()
  else:continue
print("APPROVED")
