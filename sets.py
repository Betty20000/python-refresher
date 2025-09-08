# creating a set
fruits ={"mango","orange","apple",True,1,False,0}

print(fruits)
print(len(fruits))

# set with datatypes

set1 = {1,2,3,1.23,2.0,3.4}
set2 = {"male","female","zebra","animal"}
set3 ={True, False}

print(set1)
print(set2)
print(set3)
print(type(set3))

#set() Constructor

newSet = set(("ugali","fish"))

print (newSet)

#Access Items
#you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the "in" keyword.

flowers = {"carnation","violet","iris"}

for i in flowers:
    print(i)
print("bouganvillia" in flowers)

# adding set

flowers.add("amaryllis")
flowers.add("animone")
print(flowers)

#adding sets to sets
second_flowers= {"bellflower","amerria","black-eyed susan",}
third_flowers = ["bluestar","bluebonnets"]

flowers.update(second_flowers)
print(flowers)

#adding list to set
flowers.update(third_flowers)
print(flowers)

#remove an item in a set, use the remove(), or the discard()
# NB: discard dont give error if items to remove does not exist
flowers.remove("animone")
flowers.discard("black-eyed susan")
#flowers.remove("bleeding-heart")
print(flowers)

#pop() removes an item randomly and popped item is returned


x = flowers.pop()
print(x)
print(flowers)

# clear() empty the set and del() deletes the set
flowers.clear()
print(flowers)

for x in {'apple', 'banana', 'cherry'}:
  print(x)

'''
del flowers
print(flowers)
'''

# Joining Sets 

# update(),union(),intersection(),difference(),symmetric_difference
# update() & union() joins all items in the two sets

# intersection() - keeps only the duplicates
# difference() -method keeps the items from the first set that are not in the other set(s)
#symmetric_difference() - method keeps all items EXCEPT the duplicates.

#union()
set_a= {"a","b","c",}
set_b = {1,2,3}

set_c = set_a.union(set_b)
print(set_c)

set_d= {"a","b","c",}
set_e = {1,2,3}

set_f = set_d


