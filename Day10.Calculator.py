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
num1 =int(input("What is the first number:"))
num2=int(input("What is the second number:"))

for symbol in operations:
    print(symbol)

operation_symbol = input("pick an operation from the above symbols")
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
