number=int(input("enter a number"))
star=1
space=int(number/2)
for r in range(0,int(number/2)+1):
    s=star
    for c in range(0,number):
        if (c<space):
           print(" ",end=" ")
    else:
        while s>0:
            print("*",end=" ")
            s=s-1
            c=c+1
    space=space-1
    star=star+2
    print("\n")
















number=int(input("enter a number"))
space=0
star=number
for r in range(0,number):
   s=star
   for c in range(0,number):
       if (c<space):
           print(" ",end=" ")
       else:
           while s>0:
               print("*",end=" ")
               s=s-1
               c=c+1
   space=space+1
   star=star-2
   print("\n")
#
