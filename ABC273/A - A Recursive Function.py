def func(n):
  if n == 0: return 1
  else:return func(n-1)*n
  
n = int(input())
print(func(n))
