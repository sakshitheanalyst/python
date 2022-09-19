number=int(input("enter a number"))
star=1
for r in reversed(range(0,number+1)):
    for c in range(0,r):
        print(star, end = " ")
        star=star+1
    print("\n")
