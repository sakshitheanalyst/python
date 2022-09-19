number=int(input("enter a number"))
for r in reversed(range(0,number+1)):
    for c in range(0,r):
        print(r,end = " ")
    print("\n")

