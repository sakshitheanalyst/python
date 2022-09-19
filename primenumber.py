number=int(input("enter a number"))
half = int(number/2)
isPrime = True
for i in range (2, half +1):
 if (number%i==0):
    print("not prime")
    isprime = False
    break
if isPrime:
 print("prime")

