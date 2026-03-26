while True:

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Calculator Program")
    print("Enter expression like: 8 + 7 * 5 + 7 - 10")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    expression = input("Enter calculation: ")

    if expression.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = eval(expression)
        print("Result:", result)
    except:
        print("Invalid input!")

    choice = input("Do another calculation? (yes/no): ")
    if choice.lower() != "yes":
        break
