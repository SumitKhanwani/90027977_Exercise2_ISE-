def times_or_divide(operation, num_one, num_two):
    if operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")

def add_or_subtract(operation, num_one, num_two):
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")

def get_number():
    while True:
        try:
            number = float(input())
            return number
        except ValueError:
            print("Invalid input")

def calculate():
    num_one = get_number()
    operation = input()
    num_two = get_number()

    if operation in ["*", "/"]:
        result = times_or_divide(operation, num_one, num_two)
    elif operation in ["+", "-"]:
        result = add_or_subtract(operation, num_one, num_two)
    else:
        print("Invalid input")
        return

    print(result)

def run_calculator():
    calculate()
    print("Do you want to calculate again? (y/n)")
    if input() == "y":
        calculate()
    else:
        print("Goodbye")

if __name__ == "__main__":
    run_calculator()
