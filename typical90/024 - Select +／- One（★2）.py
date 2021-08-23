n,k= map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
diff = []
diff_sum = 0
for i in range(n):
    diff.append(abs(a[i]-b[i]))
diff_sum =  sum(diff)

if(diff_sum > k):print("No")
elif(diff_sum % 2 == k %2):print("Yes")
else:print("No")
