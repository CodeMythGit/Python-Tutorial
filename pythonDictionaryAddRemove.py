student = {
    "name":"John",
    "age":35,
    "rollno":1
}

print(student)

student["rank"]=3
print(student)

student.update({"surname":"Cena"})
print(student)

#remove 5 ways
#1. using pop method
student.pop("rank")
print(student)

#2.popitem method
student.popitem()
print(student)

#using del keyword
#syntax - > del dict_obj[key]
del student["rollno"]
print(student)

#delete student object from memory
del student
# print(student)

#clear method ->to clear / empty the dict object
student = {'name': 'John', 'age': 35, 'rollno': 1, 'rank': 3, 'surname': 'Cena'}
student.clear()
print(len(student))
print(student)