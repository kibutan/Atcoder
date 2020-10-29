N = list(map(int,input().split()))
snk_list = [i+1 for i in range(N[0])]
A = []
#print(snk_list)
for i in range(N[1]):
  d = int(input())
  A = A + list(map(int, input().split()))
print(len(set(snk_list)^set(A)))
  
