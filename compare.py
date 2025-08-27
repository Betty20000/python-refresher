'''x= int(input("whats x: "))
y=int(input("whats y: "))

if x < y: print("x is less than y")
    
elif x > y: print("x is greater than y")
    
else: print("x is equal y")
   '''
# or # not 

b = 50
c = 50

if not b < c or b > c: print("b is equal to c")
else: print("b is not equal to c")

#and

score = int(input("Enter score: "))

if score >=90 and score <= 100:
    print("grade A")
elif 80 <= score < 90:
    print("grade B")
elif score < 80:
    print("grade C")


#arithmetic

d = int(input("enter d : "))
if d %2 == 0:
    print("even")
else: print("odd")


# even or odd using function

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




