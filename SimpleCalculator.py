def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("ENTER NUMBER 1\n"))
b=int(input("ENTER NUMBER 2\n"))

choice=int(input("ENTER THE CHOICE\n"))

match choice :
    
    case 1:
        print("addition is : ",add(a,b))
    case 2:
        print("substraction is : ",sub(a,b))
    case 3:
        print("multiplication is : ",multi(a,b))
    case 4:
        print("division is : ",div(a,b))
    case _:
        print("please give input 1-4")