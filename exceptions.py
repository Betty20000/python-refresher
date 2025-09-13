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

#using while loop
while True:
    try:
        x = int(input("Enter value of x : "))
    except ValueError:
        print("Value entered is not a number")
    else:
        break

print(f"Value of X is {x}")

#using functions to get and return values

def main():
        y = get_value()
        print(f"Value of Y is {y}")
def get_value():
    while True:
            try:
                
                    y = int(input("Enter value of y: "))
            except ValueError:
                    print("Value entered is not a number")
            else:
                break
    return y
            
main()

def age_func():
     your_age = get_age()
     print(f"You are {your_age} years old")
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            #return age
        except ValueError:
            print("Value entered is not a number")
        else: 
            break
    return age
        
age_func()

def age_func2():
     your_age = get_age2()
     print(f"You are {your_age} years old")
def get_age2():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Value entered is not a number")
        
age_func2()

#short hand 2

def age_func3():
     your_age = get_age3()
     print(f"You are {your_age} years old")
def get_age3():
    while True:
        try:
            return int(input("Enter your age: "))
        except ValueError:
            print("Value entered is not a number")
        
age_func3()   

#Short hand 3
def age_func4():
     your_age = get_age4()
     print(f"You are {your_age} years old")
def get_age4():
    while True:
        try:
            return int(input("Enter your age: "))
        except ValueError:
            pass          # 'pass' keyword is caching the error without printing to the user
        
age_func4()

# using `prompt` keyword  to reuse a function || NB: 'prompt' can be any name

def age_func5():
    your_age = get_age5("Enter your age: ")
    your_class = get_age5("Enter your class number: ")
    print(f"Hello your class number is {your_class} and You are {your_age} years old")
     

def get_age5(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass          # 'pass' keyword is caching the error without printing to the user
        
age_func5()

