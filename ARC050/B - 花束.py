r,b = list(map(int,input().split()))
x,y = list(map(int,input().split()))
ok = 0
ng = (r+b)//2+1
 
def is_ok(middle):
    #middle本の花束を作るとき
    global r,b,x,y
    #各1本ずつ保持したときの残数taba1
    taba1_r = r-middle
    taba1_b = b-middle
    if(taba1_b < 0 or taba1_r < 0):return False
    #その残数は赤がx-1本だけ確保できる数か、もしくは青がy-1本だけ確保できる数か?
    # print("mid:",middle," taba1_r:",taba1_r," canmake_red:",(x-1)*middle)
    # print("mid:",middle," taba1_b:",taba1_b," canmake_blue:",(y-1)*middle)
    return (taba1_r//(x-1) + taba1_b//(y-1)) >= middle
 
while (ng-ok) > 1:
    middle = (ng + ok)//2
    if is_ok(middle):
        ok = middle
    else:
        ng = middle
print(ok)
