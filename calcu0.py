import time
breaking1 = """




"""
breaking2 = """
"""

#/  /\  \
#\ /  \ /

#Welcome
name = input("Hi what is your name: ")
print(breaking2)
print("Hi "+name)
print("Welcome to the")
print("                  |   /\         |")
print("                  |  /  \  T O M |")
print("                  |   CALCULATOR |")
print("Made by")
print("Andromeda-ADC")
print(breaking2)
#number = int(input(name+" How many times would you like to use this calculator?: "))
for number1 in range(1000):
    print(breaking2)
    equ = input(name+", Which equation would you like (+ - * / ): ")
    if equ == "clear":
        exit()
    try:
        num1 = int(input("What is your first number?: "))
    except ValueError:
        print("please enter a number")
        num1 = int(input("What is your first number?: "))
    try:
        num2 = int(input("What is your second number?: "))
    except ValueError:
        print("please enter a number")
        num2 = int(input("What is your second number?: "))
    if "+" in equ:
        ans = (num1+num2)
        print(ans)

    if "-" in equ:
        ans = (num1-num2)
        print(ans)

    if "*" in equ:
        ans = (num1*num2)
        print(ans)

    if "/" in equ:
        ans = (num1/num2)
        print(ans)
    print(breaking2)
    cont = input("Continue? (y/n): ")
    if "n" in cont:
        exit()
