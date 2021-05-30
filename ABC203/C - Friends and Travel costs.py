n,k = map(int,input().split())
ab = sorted([list(map(int,input().split())) for _ in range(n)])
#少なくとも村kまでは行ける
ans = k

money = k
# print(ab)
for i in ab:
    # print(money)
    #村の名前あb「i]がK円より少なければ、ab村の住人全員から金を巻き上げたい
    if(i[0] <= money):money += i[1]
    else:
        print(money)
        exit()
print(money)
