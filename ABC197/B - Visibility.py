#https://blog.hamayanhamayan.com/entry/2021/03/27/224544
h,w,y,x = list(map(int,input().split()))
s = [input() for i in range(h)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = 0
#print(s[1][3])
 
for i in range(4):
  X = x-1
  Y = y-1
  while True:
    X += dx[i]
    Y += dy[i]
#    print("XxwYyh",X,x,w,Y,y,h)
#    print("dx,dy",dx[i],dy[i])
#    print(X <= -1,X >= w,Y <= -1,Y >= h)
    if( X <= -1 or X >= w or Y <= -1 or Y >= h):break
    else:
#      print("pass1")
#      print(s[Y][X])
      if(s[Y][X] != "#"):
        ans += 1
#        print("Pass",ans)
      else:break
print(ans+1)
