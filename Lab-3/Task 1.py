def calculate(a, b, op):
    if op == "Addition":
        return a+b
    elif op == "Subtraction":
        return a-b
    elif op == "Multiplication":
        return a*b
    elif op == "Division":
        if b == 0:
            return "Division by zero is not allowed."
        return a/b
    else:
        return "Invalid operation selected."

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nSelect an operation:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    op = input("Enter choice: ").strip()
    ans = calculate(a, b, op)
    print(f"\nResult: {ans}")

if __name__ == "__main__":
    main()