def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "division by zero is not possible!"
    else:
        return a/b
print("select operator")
print("1. add\n2. sub\n3. multiply\n4. divide")

choice = input("enter your choice (1/2/3/4): ")

n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))

if choice == '1':
    print("the addtion is: ", add(n1,n2))
elif choice == '2':
    print("the subtraction is: ", sub(n1,n2))
elif choice == '3':
    print("the multiplication is: ", multiply(n1,n2))
elif choice == '4':
    print("the division is: ", divide(n1,n2))
else:
    print("input is invalid")