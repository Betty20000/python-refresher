students = ["Hermeone","Harry","Ron"]
print(students[0])

for student in students:
    print(student)


print([student in students])

students = ["Hermeone","Harry","Ron"]
print(students[0])

for student in students:
    print(student)

for i in range(len(students)):
    print(students[i])

people = { 
    "Naomi" : "Lily",
    "Jennifer" : "Amarylis",
    "Gladys" : "Lavender"
}

for person in people :
    print(person,people[person],sep="-")


# dict{} of keys with multiple values

friends = [ 
    {"name" : "joy","age" : 23, "pet": "cat"},
    {"name": "ken","age": 34, "pet": "dog"},
    {"name": "maya","age": 25, "pet": "rabit"}
]
for friend in friends:
    print(friend["name"],friend["age"],friend["pet"],sep=", ")

#printing patterns

def main():
    print_squire(3)

def print_squire(size):
    #for each row in squire
    for i in range(size):
        #for each brick in row
        for j in range(size):
            print("|",end="")
        print()    
main()
#printing patterns short hand
def main2():
    print_squire1(3)

def print_squire1(size):
    for i in range(size):
        print("$" * size)

main2()


def main3():
    print_squire2(3)

def print_squire2(sides):
        for i in range(sides):
            print_harsh(sides)
def print_harsh(num):
        print("#" * num)
        
main3()
