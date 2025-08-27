# class point():
#     def __init__(self,input1,input2):
#         self.x=input1
#         self.y=input2
# p=point(2,8)
# p2=point(10,100)
# plusing= p.y + p2.x
    
# print(p.x)
# print(p2.x)
# print(plusing)
# print(p2.y)



# class book():
#     def __init__(self,booktitle,bookauthur):
#         self.title=booktitle
#         self.authur=bookauthur

# book1=book("Americanna","Chimmamanda Ngozi")

# print(book1.title)
# print(book1.authur)

# fruits =["orange", "banana","carrot","ovacado"]

# print(len(fruits))

# A program that adds passangers on a flight if there is enough capacity.

# create a class

class Flight():
    def __init__(self, capacity):
#create capacity        
        self.capacity=capacity
#create a list to add passangers   
        self.passangers=[]
    #create method to calculate available seats
    def open_seats(self):
        return self.capacity - len(self.passangers)
    #create method to add passenger to flight
    def add_passanger(self,name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
    
        return True
    
    
    
    
  

flight= Flight(3)
#add list of passenger to flight
people = ["Janet"]
name = input("Enter your name: ")
people.append(name)

for person in people:
    success= flight.add_passanger(person)
    if success:
        print(f"{person} Added to flight successfully")
        print(f"{flight.open_seats()} seats remaining")
    else:
        print(f"No available seat for {person} ")