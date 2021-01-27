#https://qiita.com/e869120/items/25cb52ba47be0fd418d6#3-1-bit-%E5%85%A8%E6%8E%A2%E7%B4%A2
n = int(input())
x = int(input())
a = list(map(int,input().split()))

for i in range(2**n):
  select_list = []
  for j in range(n):
    if((i>>j)&1):
      select_list.append(a[j])
  print(select_list)
