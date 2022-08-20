l_1, r_1, l_2, r_2 = map(int,input().split())
print(max(0,min(r_2,r_1)-max(l_2,l_1)))
