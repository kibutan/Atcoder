X,Y,A,B = list(map(int,input().split()))
exp = 0

while (X*A < Y and (X*A)-X <= B):
    X *= A
    exp += 1
#-1しないと、「レベルアップまであとY」のYの値だけ稼ぐことになる。
print( exp + (Y -1- X)//B )
print((Y -1- X))
print( exp + (Y - X)//B )
print(Y - X)
