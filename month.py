print("Enter a month from below\n 1 for January \n 2 for  Febuary\n 3  for March\n 4 for April\n 5 for May\n 6 for June\n 7 for July\n 8 for August\n 9 for Sepember\n 10 for October\n 11 for November\n 12 for December\n")
month=int(input("Enter a month"))
if month==2:
    print("28/29 days")
elif month==1 or month==3 or  month==5 or month==7 or month==8 or month==10 or month==12:
     print("31 days")
else:
    print("30 days")








