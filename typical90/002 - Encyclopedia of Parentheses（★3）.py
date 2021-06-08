from itertools import product
n = int(input())
s = ["(",")"]
kakko = ""
if(n %2 != 0):exit()
for i in product(s,repeat=n):
    if(i[0] == ")" or i[-1]=="("):continue
    kakko = "".join(i)
    if(kakko.count(")") != kakko.count("(")):continue
    for j in range(len(kakko)):
        start = kakko[0:j].count("(")
        end = kakko[0:j].count(")")
        if(start < end):
            # print(kakko,"is break")
            break
    else:
        #finish inner loop without break
        print(kakko)
