#calculator program
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply (num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 =int(input("What is the first number:"))
    for symbol in operations:
        print(symbol)
    stop_loop = False
    while not stop_loop:
        operation_symbol = input("pick an operation from the above symbols")
        num2=int(input("What is the next number:"))
        # if operation_symbol == "+":
        #     add(num1,num2)
        # elif operation_symbol == "-":
        #     subtract(num1,num2)
        # elif operation_symbol == "*":
        #     multiply(num1,num2)
        # elif operation_symbol == "/":
        #     divide(num1,num2)

        called_operation = operations[operation_symbol]
        hereby =called_operation(num1,num2)

        print(f"{num1}{operation_symbol}{num2}={hereby}")
        should_continue =input(f"Do you wish to continue with {hereby}, type yes or no").lower()
        if should_continue =="no":
             stop_loop = True
             calculator()
        elif should_continue =="yes":
                num1 = hereby
calculator()