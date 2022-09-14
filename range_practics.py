#for i in range (10):
#    print(i)

#for i in range (5,10):
 #   print(i)

expenses=[1200,1500,1700,1300]
total=0
for i in range (len(expenses)):
      expense=expenses[i]
      print(f'month {i+1},expense:{expense}')
      total+=expense

      print("tatal expenses:",total)

