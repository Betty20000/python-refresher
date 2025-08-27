#list comprehension

names = ["John", "James","Enn","Jimmy","Michael"]

j_names = []

for name in names:
    if "J" in name:
        j_names.append(name)
print(j_names)

#Short hand of above

names2 = ["John", "James","Enn","Jimmy","Michael"]
j_names2 = [ name for name in names2 if "J" in name]

print(j_names2)

# copy list content to another

flowers = ["tulip","iris","carnation","lily","daisy"]

copy_flowers =[flower for flower in flowers]

print(copy_flowers)

#calculation

numbers = [2,3,4,5,6,7,8,9,10]

squares = [s*s  for s in numbers]
print(squares)

#task

animals = ["lion","tiger","monkey","elephant","flog"]

filtered_animals = []
for animal in animals:
    filtered_animals.append(animal.title())
print(filtered_animals)

filtered_animals2 = [animal.title() for animal in animals]

print(filtered_animals2)


