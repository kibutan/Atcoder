def g_1(x):
  return int("".join(sorted(str(x),reverse = True )))
def g_2(x):
  return int("".join(sorted(str(x))))
def f(x):
  return g_1(x)-g_2(x)

n,k = list(map(int,input().split()))
a = n
#print(f(n))
for i in range(k):
#  print("looping f(a)",f(a))
  a = f(a)
print(a)
