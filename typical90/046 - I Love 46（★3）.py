from collections import Counter

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a_46 = [i%46 for i in a]
b_46 = [i%46 for i in b]
c_46 = [i%46 for i in c]
a_cnt = Counter(a_46)
b_cnt = Counter(b_46)
c_cnt = Counter(c_46)
# print(a_cnt)
# print(b_cnt)
# print(c_cnt)
sum = 0
for i,i_cnt in a_cnt.items():
    for j,j_cnt in b_cnt.items():
        for k,k_cnt in c_cnt.items():
            if((i+j+k)%46 == 0):sum += (i_cnt*j_cnt*k_cnt)
print(sum)
