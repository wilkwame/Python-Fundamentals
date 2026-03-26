
while True:

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("      Welcome to the Calculator Program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    first_number = float(input("Enter first number: "))
    second_number = input("Enter operator (+, -, *, /): ")
    operator = input("Enter operator (+, -, *, /): ")
    if operator == "+":
        print("Result: ", first_number + second_number)

    elif operator == "/":
        if second_number != 0:
            print("Result: ", first_number / second_number)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "*":
        print("Result: ", first_number * second_number)

    elif operator == "-":
        print("Result: ", first_number - second_number)
    
    else:
        print("Invalid operator!")

    choice = input("Do another calculation? (yes/no): ")
    if choice.lower() != "yes":
        break