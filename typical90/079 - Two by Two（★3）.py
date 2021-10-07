h,w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
cnt = 0
diff = [[0 for _ in range(w)] for _ in range(h)]
# print(diff)
for i in range(h-1):
    for j in range(w-1):
        diff[i][j] = -1*diff[i][j] + (b[i][j] - a[i][j])
        diff[i+1][j] += diff[i][j] 
        diff[i][j+1] += diff[i][j]
        diff[i+1][j+1] += diff[i][j]
        
        cnt += abs(diff[i][j])
# print(diff)

for k in range(h-1):
    if(a[k][w-1] +diff[k][w-1] != b[k][w-1]):
        # print("No",a[k][w-1] +diff[k][w-1], b[k][w-1])
        print("No")
        exit()
for l in range(w):
    if(a[h-1][l] +diff[h-1][l] != b[h-1][l]):
        print("No")
        exit()

print("Yes")
print(cnt)
