W,H,N = list(map(int,input().split()))
x = [list(map(int,input().split())) for _ in range(N)]
#print(x)
x_f=0
x_t=W
y_f=0
y_t=H
for i in range(N):
  if(x[i][2] == 1):
    x_f = max(x[i][0],x_f)
#    print("1:"+str(x_f))
  elif(x[i][2] == 2):
    x_t = min(x[i][0],x_t)
#    print("2:"+str(x_t))
  elif(x[i][2] == 3):
    y_f = max(x[i][1],y_f)
#    print("3:"+str(y_f))
  elif(x[i][2] == 4):
    y_t = min(x[i][1],y_t)
#    print("4:"+str(x_t))
if((x_t-x_f)>0 and (y_t-y_f)>0):print((x_t-x_f)*(y_t-y_f))
else:print(0)
  
# 5-2*
