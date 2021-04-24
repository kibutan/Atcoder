n = int(input())
s = list(input())
q = int(input())
tab = [list(map(int,input().split())) for _ in range(q)]
def main():
  for i in range(q):
    a = tab[i][1]
    b = tab[i][2]
    if(tab[i][0] == 1):s[a-1],s[b-1] = s[b-1],s[a-1]
    elif(tab[i][0] == 2):s[:n],s[n:] = s[n:],s[:n]
  print("".join(s))

main()
