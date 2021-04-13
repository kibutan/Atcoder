n = int(input())
string = "0"
for i in range(0,10):
    string = str(i) + str(i) + str(i)
#    print(string)
    if string in str(n):
        print("Yes")
        exit()
    else:continue
print("No")
