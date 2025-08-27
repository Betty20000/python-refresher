#list
# creating a list
items = [1,4,"go",'come',25.2]

#features of list
#can have duplicate,mutable,can take diff. variables
items2=["red","red",1,1,1]

#accessing elements - index

print(items[2])

items[1] = "green"

print(items[-1])

# add item to the list

items.append("rest")
print(items)
# remove item
del items[0]

fruits =["ovacado","mango","oranges","melon","banana"]

fruits.remove(fruits[0])
print(fruits)
fruits.remove(fruits[0])
print(fruits)
#accessing multidemensional list

my_list = [[1,2,3,],"Nest", [4,5,6]]

print(f"{my_list [0][0]} , {my_list[2]}")

# add item to the list using methods

#append(),insert(),extend()
students = ["koman","fred","ashley"]
other_students= ["jane","vincent"]

# at the end 

students.append("delmas")
#another list content to the end of another list
students.extend(["jairus","solo"])
students.extend(other_students)

#any specific position - list.insert(position,value)
students.insert(0,"dama")
print(students)
print(len(students))

#input() method to add items to a list
int() #coverts to integer
# ask number of items to be in the list,create empty list,loop to input,append
n = int(input("enters  number of elements: "))
numbers = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

print(numbers)

# split() method

sentence = "I am John"

sentence.split()

print(sentence)

my_numbers = input("Enter a list of numbers").split()

print(my_numbers)
for f in my_numbers:
    print(f)

for k in range(0,3):
    print("hi world")

# accepting input to list using for loop

element_numbers = int(input("Enter the number of elements"))
your_numbers = input("Enter a list of numbers").split()

for num in range(0,element_numbers):
    your_numbers[num] = int(your_numbers[num])
    print(your_numbers)
    



    
    


