#simple calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
       return "Cannot dived by zero"


print("Welcome to the Simple Calculator")
print("Please choose an operation: 1: Addition  2: Substraction  3: Multiplication  4: Division")

choice= input("enter your choice 1/2/3/4: ")
num_1= float(input("enter the first number: "))
num_2= float(input("enter the second number: "))

if choice=="1":
    print("result:", add(num_1,num_2))
elif choice=="2":
     print("result:", sub(num_1,num_2))
elif choice=="3":
     print("result:", mult(num_1,num_2))
elif choice=="4":
     print("result:", div(num_1,num_2))
else:
    print("Invalid Choice")