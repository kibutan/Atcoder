s1 = input()
s2 = input()
s3 = input()
s_set = set(["ABC", "ARC", "AGC" , "AHC"])
print(*(s_set^(set([s1,s2,s3]))))