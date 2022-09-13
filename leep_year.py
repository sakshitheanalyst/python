year=int(input("Enter a year="))
if year%100==0 and year%400==0:
    print("leep_year")
elif year%4==0 and year%100!=0:
    print("leep_year")
else:
    print("not_leep_year")


