# key:value
student = {
    "name":"John",
    "age":45,
    "year":1976
}

#properties
#ordered*, changeable,doest not allow duplicate values in dict
print(student)

student["age"] = 30
print(student)

student = {
    "name":"John",
    "age":45,
    "year":1976,
    "age":31
}
print(student)

#how to calc length
print("length : ",len(student))

#type 
print("Type : ",type(student))
