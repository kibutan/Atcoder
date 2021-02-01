# 参考
# https://qiita.com/gogotealove/items/11f9e83218926211083a

# switch n, light bulb m
n,m = list(map(int,input().split()))

# k[i(i:1-m)]  = light bulb No.i has k switches (k[i]:1-n)
# s[i(i:1-m)]  = light bulb No.i connected these switches (k[i]:1-n)
ks = [list(map(int,input().split())) for _ in range(m)]

# p[i(i:1-m)]  = if(p[i] == sum(s[i][j] (j:1-n) is ON(1)) % 2) when light bulb No.i's power is  ON
p = list(map(int,input().split()))

# How many ON swithes each light bulb = cnt 
# When cnt%2 == p[i], light bulb No.i's power is ON
cnt =0

# When All Light bulb is ON, ans++
ans = 0

#ks[] devide into k[] and s[] 
k = []
s = []
for i in range(m):
  k.append(ks[i][0])
  s.append(ks[i][1:])

#debug----
#print("ks",ks)
#print("k",k)
#print("s",s)
#for i in range(2**n):
#  flag = 1
#  bit = []
#  for j in range(n):
#    if((i >> j)&1):
#      bit.append(j+1)
#  print(bit)
#-----

#bit全探索
for i in range(2**n):
#when bit == 1, bit[] appended (j+1) that name of switches
#ex.)there is swithes{1,2}, when bit[] = {},{1},{2},{1,2}
  bit = []
  for j in range(n):
    if((i >> j)&1):
      bit.append(j+1)
#  print("bit",bit)
  # before bit[] change (before bit[] change {} to {1]),
  # search swithes connected each bulb ON or OFF

  # inclement k can't use because k[] used for number of switches.
  # so I used variable x,y temporary. that is UNCO-DE, I know enough.
  # by the way, search (bit[] in s[] or not), for 1 to bulb m. 
  for x in range(m):
    cnt = 0
    for y in bit:

#debug----      
#      print("i",i)
#      print("s[",x,"]=",s[x],"have i = ",i," is",i in s[x])
#debug-----
      # when bit[] in swithes connected Bulb, cnt++
      if(y in s[x]):cnt += 1
#    print("p[",x,"]=",p[x]," equal to cnt = ",cnt," % 2 is",cnt % 2 == p[x])
    #When each bit[-1], == decided cnt, search p[x] == cnt % 2  
    if(cnt % 2 != p[x]):
    #when cnt != p[x], search about next bit
#      print("Pass")
      break
    #WHEN ALL BIT->SWITCHES MATCH UP p[i]== ALL BULBS ON, ans++  
    elif(cnt%2 == p[x] and x == (m-1)):ans+=1
print(ans) 
