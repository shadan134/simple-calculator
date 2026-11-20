"""
Simple Calculator
=================

A beginner-friendly command-line calculator written in Python.

Features:
    - Addition, subtraction, multiplication, and division
    - Input validation for non-numeric values
    - Safe handling of division by zero
    - Interactive menu loop

Author: Shadan
"""

from typing import Union

Number = Union[int, float]


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu() -> None:
    """Display the calculator menu."""
    print("=" * 40)
    print("         Simple Calculator")
    print("=" * 40)
    print("Select an operation:")
    print("  1. Add       (+)")
    print("  2. Subtract  (-)")
    print("  3. Multiply  (*)")
    print("  4. Divide    (/)")
    print("  5. Exit")
    print("-" * 40)


def main() -> None:
    """Run the interactive calculator."""
    display_menu()

    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
    }

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        operation, symbol = operations[choice]

        try:
            result = operation(num1, num2)
        except ZeroDivisionError as error:
            print(f"\nError: {error}")
            continue

        print(f"\nResult: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()
