from itertools import product
 
x = input()
x_list = []
n = int(input())
# a,b = list(map(int,input().split()))
s = [list(map(str,input())) for i in range(n)]
array = [[-1 for i in range(11)] for j in range(50001)]
# array = [[]]
# print(s[1][0])
cnt = 0
for i in range(len(x)):
    x_list.append(x[i])
# print(x_list)
 
for i in range(len(s)):
    for j in range(len(s[i])):
        array[cnt][j] = x_list.index(s[i][j])
    # print(sorted(array))
    cnt += 1
 
sorted_array = sorted(array)
# print(sum(sorted_array[1]))
for i in range(len(sorted_array)):
    if sum(sorted_array[i]) == -11:continue
    for j in range(len(sorted_array[i])):
        # if sorted_array[i][0] == -1:break
        if sorted_array[i][j] == -1:continue
        else:print(x[sorted_array[i][j]],end="")
    print()
