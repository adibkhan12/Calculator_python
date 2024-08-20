from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
new_calculation = False
while not new_calculation:
    calculation_over = False

    first_number = float(input("What's the first number?: "))
    while not calculation_over:
        print("+\n- \n* \n/")
        operation = input("Pick an operation")
        second_number = float(input("What's the next number?:"))
            # OPTION_1
        if operation in operations:
            result = operations[operation](first_number, second_number)
            print(f"{first_number} {operation} {second_number} = {result}")

            # OPTION_2
        # if operation == "+":
        #     answer = add(first_number, second_number)
        #     print(f"{first_number} {operation} {second_number} = {answer}")
        # elif operation == "-":
        #     answer = subtract(first_number, second_number)
        #     print(f"{first_number} {operation} {second_number} = {answer}")
        # elif operation == "*":
        #     answer = multiply(first_number, second_number)
        #     print(f"{first_number} {operation} {second_number} = {answer}")
        # elif operation == "/":
        #     answer = divide(first_number, second_number)
        #     print(f"{first_number} {operation} {second_number} = {answer}")

            # OPTION_3
        # answer = operations[operation](first_number, second_number)
        # print(f"{first_number} {operation} {second_number} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if cont == "y":
            calculation_over = False
            first_number = result
        else:
            calculation_over = True
            print("\n" * 100)
