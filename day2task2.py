num1=int(input("ENTER YOUR FIRST NUMBER:"))
num2=int(input("ENTER YOUR SECOND NUMBER:"))
op=input("ENTER THE OPERATOR:")
if op=="add":
    addition=num1+num2
    print(addition)
elif op=="sub":
    subtraction=num1-num2
    print(subtraction)
elif op=="div":
    division=num1/num2
    print(division)
elif op=="mul":
    multiplication=num1*num2
    print(multiplication)
else :
    print('ENTERED OPERATOR IS WRONG!!')
