n = int(input())
s = [input() for _ in range(n)]
mark = ["H","D","C","S"]
number = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]
# print(s,len(set(s)) == len(s))
if( len(set(s)) != len(s) ):
    print("No")
    exit()
else:
    for i in range(n):
        if(s[i][0] not in mark):
            print("No")
            exit()
        if(s[i][1] not in number):
            print("No")
            exit()
print("Yes")
