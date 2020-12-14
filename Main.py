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
print("               |   /\         |")
print("               |  /  \  T O M |")
print("               |   CALCULATOR |")
print("Made by")
print("Andromeda-ADC")
print(breaking2)
number = int(input(name+" How many times would you like to use this calculator?: "))
for number1 in range(number):
    equ = input("Which equation would you like (+ - * / ): ")
    if equ == "clear":
        exit()
    num1 = int(input("What is your first number?: "))
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
    print(breaking1)
    wait = input("Press Enter To Continue.")
