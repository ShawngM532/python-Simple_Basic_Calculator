#simple Python Calculator
#by shawngM532--> GitHub

state = ['+', '-', '*', '/']


def Add(a,b):
    c = a + b
    print(c)

def Subtract(a,b):
    c = a - b
    print(c)

def Multiply(a,b):
    c = a * b
    print(c)

def Divide (a,b):
    if (b<=0):
        print("Error cant divide")
    else:
        c = a / b
        print(c)    


def Calculator():
    x = input("Enter x:")
    y = input("Enter y:")
    p = int(x)
    q = int(y)

    action = input("Enter the action needed: ")

    if (action == state[0]):
        return Add(p, q)
    elif(action == state[1]):
        return Subtract(p,q)
    elif(action == state [2]):   
        return Multiply(p,q)
    else:
        return Divide(p,q)
    

Calculator()


