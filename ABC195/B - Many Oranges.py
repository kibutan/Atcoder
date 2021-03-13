a,b,w = list(map(int, input().split()))
w = w *1000
ans =[]
to = (w) // a
fr = (w) // b
#print(fr,to)
for i in range(fr,to+1):
#  print(i)
  if(a <= w/i <= b): ans.append(i)
if(ans == []):
  print("UNSATISFIABLE")
  exit()
print(ans[0],ans[-1])
