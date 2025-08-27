#if statements
a=20
b=100
module = 100%2

if a<b:
        print("a is less than b")
else:
        print("b is greater than a")
#ask user for their name

name =input("Whats your name: ").strip().capitalize()
name= name.strip().capitalize()
name=name.title()

#splitting
first,last = name.split(" ")

#say hello to user
print(f'hello, {first}')ee
print("hello,",end="")
print(name)

print(module)

converting inputs

house = input("Enter the name of your house: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
net = int(input("Enter your networth: "))


print(f"You live in {house}, you are {age} years old and your height is {height:.3f}.\n Your net worth is {net:,} dollars")

height=round(height,2) 


print("your height is:",height)
