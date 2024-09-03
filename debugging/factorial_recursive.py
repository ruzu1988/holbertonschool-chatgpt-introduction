#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0;
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non.negative integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError
        f = factorial(n)
        print(f)
    except ValueError:
        print("Error: Please provide a non-negative integer.")
        sys.exit(1)

