def digitSum(n):
    # 数値を文字列に変換
#    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, n))
    # 合計値を返す
    return sum(array)
N = input()
ans = 0
if(len(N)==1):
  if(int(N)%3 == 0):
    print(0)
    exit()
  else:
    print(-1)
    exit()
if(len(N) == 2):
  if(int(N)%3 == 0):
    print(0)
    exit()
  elif(int(N[0])%3 ==0 or int(N[1])%3 ==0):
    print(1)
    exit()
  else:
    print(-1)
    exit()
#3桁以上
if(digitSum(N)%3 == 0):
  print(0)
  exit()
elif(digitSum(N)%3 == 1):
#  print(1)
  if(1 or 4 or 7) in N:ans = 1
  else: ans = 2
  print(ans)
elif(digitSum(N)%3 == 2):
#  print(2)
  if(2 or 5 or 8) in N:ans = 1
  else: ans = 2
  print(ans)
