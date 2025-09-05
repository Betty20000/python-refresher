#While loop
import sys
while True:
    n = int(input("Enter number of times for cat to meow: "))
    if n <= 0:
        continue
    else:
        break
for _ in range(n):
    print("meow")

#Short hand while true loop

while True:
    try:

        x = int(input("Enter number of times for cat to meow again: "))

    except ValueError:
        print("invalid input")
        sys.exit(1)

    if x > 0:
        break
    
for _ in range(x):
    print("Meeeeow")