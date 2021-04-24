n = int(input())
s = list(input())
q = int(input())
tab = [list(map(int,input().split())) for _ in range(q)]

def main():
  dict = {}
  for i in range(len(s)):
    dict[str(i+1)] = s[i]
#  print(dict)
  for j in range(q):
    if(tab[j][0]==1):dict[str(tab[j][1])],dict[str(tab[j][2])]=dict[str(tab[j][2])],dict[str(tab[j][1])]
    elif(tab[j][0] == 2):
      for k in range(n):
        dict[str(k+1)],dict[str(k+1+n)]=dict[str(k+1+n)],dict[str(k+1)]
  print("".join(dict.values()))
main()
