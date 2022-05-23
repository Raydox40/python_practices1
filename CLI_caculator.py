
print("welcome to cli calculator")

user_input = input("Which operation will you like to perform?\n['+','-','*','/','%']: ")

 #user iput number
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the Second number:"))
    # perform addition
if user_input == "+":
    print(number1 + number2)

    # perform substraction
elif user_input == "-":
    print(number1 - number2)

    # perform multiplication
elif user_input == "*":
    print(number1 * number2)

    # perform division
elif user_input == "/":
    print(number1 / number2)

    # perform modulus operation
elif user_input == "%":
    print(number1 % number2)

else:
    print("Invalid operation.Enter correct number...")