#コードテストが動かないため途中で放り出した。

S = input()
len_bit = len(S)-1
T = []
temp = 0
ans = 0


for i in range(2 ** len(S)):
  list = []
  print("pattern {}: ".format(i), end="")
  for j in range(len_bit):
    if((i >> j) & 1):
      temp = int(T)
    else:
      T.append(S[j+1])
  Temp = int(T)
print(T)
