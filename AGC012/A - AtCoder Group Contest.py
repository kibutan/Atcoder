N = int(input())
a = sorted(list(map(int,input().split())),reverse = True)
ans = [i for i in a[1::2]]
ans = ans[:N]
print(sum(ans))
