import sys
try:
    x=int(input("Enter value of x : "))
    y=int(input("Enter value of x : "))
except ValueError:
    print("Error: invalid input")
    sys.exit(1)

try:
    sum= x / y
except:
    ZeroDivisionError
    print("Error: Cannot divide by 0")
    sys.exit(1)

print(f"value of {x} / {y} is {sum}")