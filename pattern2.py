number=int(input("Enter a number="))
star=1
for r in range(0,number):
    for c in range(0,r+1):
        print(star, end = " ")
        star = star+1


    print("\n")


