def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
#    print("sum:"+str(sum(array)))
    return sum(array)

N = int(input())
S = str(N)
ans = 0
if(len(str(N))==1):
  if(N%3 == 0):
    print(0)
    exit()
  else:
    print(-1)
    exit()
if(len(S) == 2):
  if(N%3 == 0):
    print(0)
    exit()
  elif(int(S[0])%3 ==0 or int(S[1])%3 ==0):
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
#  print("1" in S or "4" in S or "7" in S)
  if("1" in S or "4" in S  or "7" in S):ans = 1
  else: ans = 2
  print(ans)
elif(digitSum(N)%3 == 2):
#  print("2" in S or "5" in S or "8" in S)
  if("2" in S or "5" in S or "8" in S):ans = 1
  else: ans = 2
  print(ans)
