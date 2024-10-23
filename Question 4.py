#simple calculator program
#the function of the calculator



def calculator(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        if num2 !=0:
         return num1/num2
        else:
            return "error!"
    else:
        return "invalid operation!"

#inputs from the user
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation: ")
#claculation

results=calculator(num1,num2,operation)

print(results)
