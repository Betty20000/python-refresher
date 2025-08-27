people = [
    {"name":"James","house":"Kilimanjaro"},
    {"name":"Alan","house":"longonot"},
    {"name":"Zeph","house":"mt kenya"}
          ]
# def define(person):
#     return person["name"]

people.sort(key=lambda place:place["house"])

print(people)

student = [
    {"school": "Alliance","hobby":"painting","snacks":"banana"},
    {"school": "Tumutumu","hobby":"swimming","snacks":"salmon"} , 
    {"school": "Bishop gatimu","hobby":"dancing","snacks":"mango"}     
           
           ]
def define_sort(place):
    return place["snacks"]
student.sort(key=define_sort)
student.sort(key=lambda value:value["school"])
print(student)

