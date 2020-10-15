def main():
  N = int(input())
  A = list(map(int,input().split()))
  sum = 1
  if 0 in A:
    print(0)
    return
  for i in A:
    sum *= i
    if(sum > 1000000000000000000):
      print(-1)
      return
  print(sum)
main()
