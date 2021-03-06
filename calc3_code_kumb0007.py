#!/usr/bin/python3

#	Name Ditah K
#	Program name & Version: Calculator 2
#	Date: 04/10/2021
#	Version: 3.0

#	Defining function for menu
def	displ_menu():
    print("\nMenu Options:\n\t+: To Add \n\t-: To Subtract\n\t*: To Multiply\n\t/: To Divide")

#	Defining function to prompt user for input
def get_float(prompt):
    num = float(input(prompt))
    return num

#	Defining function for zero
def iszero(num):
	if num == 0:
		return True
	else:
		return False

#	Defining function for Addition
def add():
    first_num = get_float("Enter your first number: ")
    second_num = get_float("Enter your second number: ")
    result = first_num + second_num
    print(f"-> Result of calculation: {first_num} + {second_num} = {result}")

#	Defining function for Subtraction
def subtraction():
    first_num = get_float("Enter your first number: ")
    second_num = get_float("Enter your second number: ")
    result = first_num - second_num
    print(f"-> Result of calculation: {first_num} - {second_num} = {result}")
	
#	Defining function for multiplication
def multiply():
    first_num = get_float("Enter your first number: ")
    second_num = get_float("Enter your second number: ")
    result = first_num * second_num
    print(f"-> Result of calculation: {first_num} * {second_num} = {result}")
	
#	Defining function for Division
def divide():
    first_num = get_float("Enter your first number: ")
    second_num = get_float("Enter your second number: ")
    while (second_num == 0):
        second_num = get_float("Can not be 0, Enter something else: ")
    result = first_num / second_num
    print(f"-> Result of calculation: {first_num} / {second_num} = {result}")
	
#Script Begins, we call the display function
displ_menu()
operator = input("\nEnter operator (q to quit): ")
while (operator != 'q'):
    if (operator == '+'):
        add()
        displ_menu()
        operator = input("\nEnter operator (q to quit): ")
    elif (operator == '-'):
        subtraction()
        displ_menu()
        operator = input("\nEnter operator (q to quit): ")
    elif (operator == '*'):
        multiply()
        displ_menu()
        operator = input("\nEnter operator (q to quit): ")
    elif (operator == '/'):
        divide()
        displ_menu()
        operator = input("\nEnter operator (q to quit): ")
    else:
        print("Invalid operator provided. Enter correct operator.")
        displ_menu()
        operator = input("\nEnter operator (q to quit): ")

print("Closing calculator.")
