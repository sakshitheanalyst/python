number=int(input("enter a number"))
rev=0
while number>0:
    rem=number%10
    rev=rev*10+rem
    number=int(number/10)
print(rev)

