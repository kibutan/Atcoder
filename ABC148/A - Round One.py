A= [int(input()) for _ in range(2)]
selections = [1,2,3]
print(list(set(A)^set(selections))[0])
