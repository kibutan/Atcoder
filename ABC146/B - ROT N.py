def Rotn(c):
    return ((c - 65)%26) + 65

n = int(input())
s = input()
for i in range(len(s)):
    # print("test",s[i],ord(s[i]),end=":")
    # print( chr( ord(s[i]) + n ) ,end=":")
    print(chr(Rotn(ord(s[i]) + n)),end="")
