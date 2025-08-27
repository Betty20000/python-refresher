#if else,elif,else

a= 100
b= 50
#if elif else
if a<b:
    print("B is greater")
elif a>b:
    print("A is greater")
else:
    print("A is equal to B")
#if else
if a == b:
    print("both are equal")
else:
    print("A and B are not equal")

#short hand if 

if a>b: print("A is the king")

#short hand if else

print("we are the same") if a==b else print("A and B cannot be the same")
print("B is the queen") if a>b else print("A is the master")

#short hand if elif else

flower = "thorns"

print("flower is  a rose") if flower == "rose" else print("flower is a not a rose")  if flower == "bouganvellia" else print("I cant know for sure")

#Logical operators AND, OR, NOT

#1. AND - is used to combine conditional statements. compares if both conditions are true

x = 10000
y = 20000
z = 300

if z<y and y>x:
    print("all of them are true")
else: 
    print("one or both are not true")

# OR - one has to true
if z>y or y>x:
    print("one of them are true")
else: 
    print("none is true")

# NOT- is used to reverse the result of the conditional statement:
if not x>y:
    print("x is not greater than y")
else: 
    print("y is greater")

# Nested If - if statements inside other if statements

i = 100
j = 200
k= 300

if k < 400:
    print("k is less than 400")
    if k > i:
        print("k is also greater than 100")
        if k >j :
            print("k is also greater 200 ")
            if k == 300 :
                print("k is definetly 300 ")
else:
    print("k is greater than 400 or less than 100")

# The pass Statement - if statement with no content, put in the pass statement to avoid getting an error

m = True

if m == True:
    pass

# match statements - used to test all the blocks to act on the specified condition
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
#The value _ will always match, put it the last one
colors = 9 
match colors:
    case 1:
      print("Red")
    case 2:
      print("orange")
    case 3:
      print("yellow")
    case 4:
      print("green")
    case 5:
      print("blue")
    case 6:
      print("indigo")
    case 7:
      print("violet")
    case _:
      print("color not found")

#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

day = 6
month = 5 
match day:
    case 1|2|3|4|5 if month ==4:
        print("a weekday in April")
   
    case 6|7 if month ==5:
      print("a weekend in May")
    case _:
      print("no match")