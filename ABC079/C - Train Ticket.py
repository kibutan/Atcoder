from itertools import product
import copy
s = input()
abcd = [int(c) for c in s]
#print(abcd)
tmp = []
for op in product(["+","-"],repeat=3):
    # print(op)
    tmp = copy.deepcopy(abcd)
    # print(tmp)
    for i in range(3):
        if(op[i] == "-"): tmp[i+1] = -tmp[i+1]
    if(sum(tmp) == 7):
        # print(tmp)
        # print(abs(abcd[0]),op[0],abs(abcd[1]),op[1],abs(abcd[2]),op[2],abs(abcd[3]),"=7")
        ans = str(abs(abcd[0]))+op[0]+str(abs(abcd[1]))+op[1]+str(abs(abcd[2]))+op[2]+str(abs(abcd[3]))+"=7"
        print(ans)
        exit()
    else:continue
