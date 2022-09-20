number=int(input("enter a number="))
star=1
space=int(number/2)
for  r in range(0,number):
    s=star
    if r<=int(number/2):
        for c in range(0,number):
            if (c<space):
                print(" ",end=" ")
            else:
                while s>0:
                    print("*",end=" ")
                    s=s-1
        space=space-1
        star=star+2
        print("\n")



    #     space=space+1
    #     star=star-2
    #     for c in range(0,number):
    #          if (c<space):
    #              print(" ",end=" ")
    #          else:
    #              while s > 0:
    #                  print("*", end=" ")
    #                  s = s - 1
    # print("\n")




