n = int(input())
xy = [tuple(map(int,input().split())) for i in range(n)]
xy_set = set(xy)
ans = 0
for i in range(n):
#  print("i: ",xy[i][0],xy[i][1])
  A = [xy[i][0],xy[i][1]]
  for j in range(i+1,n):    
    B = [xy[j][0],xy[j][1]]
#    delta_x = B[0] - A[0]
#    delta_y = B[1] - A[1]
#    print("A",A)
#    print("B",B)
#    print("j: ",xy[j][0],xy[j][1])
#    print("Delta x,y:" ,xy[j][0]-xy[i][0],xy[j][1]-xy[i][1] )
#    C= (A[0]+(delta_y), A[1]-(delta_x))
#    D= (B[0]+(delta_y), B[1]-(delta_x))
#    E= (A[0]-(delta_y), A[1]+(delta_x))
#    F= (B[0]-(delta_y), B[1]+(delta_x))
    if((((A[0]+(B[1] - A[1]),A[1]-(B[0] - A[0])) in xy_set and (B[0]+(B[1] - A[1]), B[1]-(B[0] - A[0])) in xy_set))):ans = max(ans,(B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
print(ans)
