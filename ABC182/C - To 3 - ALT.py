def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)
N = int(input())
S = str(N)
ans = 0

if(digitSum(N)%3 == 0):print(0)
elif(digitSum(N)%3 == 1):
  if("1" in S or "4" in S or "7" in S):print(1)
  elif(len(S)<=2):print(-1)
  else:print(2)
elif(digitSum(N)%3 ==2):
  if("2" in S or "5" in S or "8" in S):print(1)
  elif(len(S) <= 2):print(-1)
  else:print(2)
