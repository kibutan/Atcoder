n  = int(input())
s = [input() for _ in range(n)]

s_set = sorted(list(set(s)),reverse = True)
print(s_set)

for i in range(len(s_set)):
  if( "!"+s_set[i] in s_set[i:]):
    print(s_set[i])
    exit()
  else:continue
print("satisfiable")
  
