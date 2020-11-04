X,Y,A,B = list(map(int,input().split()))
exp = 0

while(X*A<Y or X+B<Y):
  if (X*A) - X <= B:
    X *= A
    exp += 1
    print("X:"+str(X))
    print("exp:"+str(exp))
#    print(exp)
  else:
    X += B
    exp += 1
    print("X:"+str(X))
    print("exp:"+str(exp))
#    print(exp)
