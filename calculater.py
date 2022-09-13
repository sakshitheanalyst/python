operater=str(input("Enter a Operater(+,_,*,%,/)="))
number_1=int(input("Enter a Number_1="))
number_2=int(input("Enter a Number_2="))
if operater=='+':
    print(number_1+number_2)
elif operater=='_':
    print(number_1-number_2)
elif operater=='*':
    print(number_1*number_2)
elif operater=='%':
    print(number_1%number_2)
elif operater=='/':
    print(number_1/number_2)
else:
    print("correct_operater")
