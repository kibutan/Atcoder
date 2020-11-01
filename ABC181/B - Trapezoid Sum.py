N = int(input())
ans = 0
list_ans = [[0] * 2 for i in range(N)]
for i in range(N):
  list_ans[i] = list(map(int,input().split()))
  ans = ans + sum(list(range(list_ans[i][0], (list_ans[i][1]+1))))
print(ans)
