S = input().split()
alphabet = ["abcdefghijklmnopqrstuvwxyz"]
if(set(S[0])^set(alphabet[0])):print(sorted(list(set(S[0])^set(alphabet[0])))[0])
#print(sorted(alphabet[0]))
else:print("None")
