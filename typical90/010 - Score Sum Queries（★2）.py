from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

n = int(input())
cp = [list(map(int,input().split())) for i in range(n)]

p1 = [(0,0)]
p2 = [(0,0)]
# p1_acc = []
# p2_acc = []
j = 0
score_1 = 0
student_number_1 = [0]
score_2 = 0
student_number_2 = [0]
for i in cp:
    j += 1
    if i[0] == 1:
        score_1 += i[1]
        p1.append((j,score_1))
        student_number_1.append(j)
    else:
        score_2 += i[1]
        p2.append((j,score_2))
        student_number_2.append(j)
# print(p1,p2)
# print(student_number_1,student_number_2)

q = int(input())
lr = [list(map(int,input().split())) for i in range(q)]
l,r =[list(i) for i in zip(*lr)]
# print(l)
for i in range(q):
    index_1_l = bisect_left(student_number_1,l[i])
    index_1_r = bisect_right(student_number_1,r[i])
    index_2_l = bisect_left(student_number_2,l[i])
    index_2_r = bisect_right(student_number_2,r[i])

    print(p1[index_1_r-1][1]-p1[index_1_l-1][1],p2[index_2_r-1][1]-p2[index_2_l-1][1])
