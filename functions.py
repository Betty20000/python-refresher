#calling functions inside other funtions
def main2():
    x = int(input("Enter value of x: "))
    print("square of x is:", square(x))

def square(n):
    return n**2 # can be written as pow(n,2)
main2()

def main():
    m = int(input("Enter value of m: "))
    if is_even(m):
        print("Even")
    else:
        print("Odd")
def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False
main()

