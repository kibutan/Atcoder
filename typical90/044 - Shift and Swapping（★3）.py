n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
txy = [list(map(int,input().split())) for _ in range(q)]
t,x,y = [list(i) for i in zip(*txy)]
x = [i-1 for i in x]
y = [i-1 for i in y]
# print(t,x,y)
shift = 0
for i in range(len(t)):
    if t[i] == 1:
        a[(x[i]-shift)%n], a[(y[i]-shift)%n] =  a[(y[i]-shift)%n], a[(x[i]-shift)%n]
        # print("t1:",a,a[(x[i]-shift)], a[y[i]-shift])
    elif t[i] == 2:
        shift += 1
        # shift %= n
        # print("t2:",shift)
    elif t[i]==3:
        # print("t3:",a[(x[i]-shift)%n])
        print(a[(x[i]-shift)%n])
