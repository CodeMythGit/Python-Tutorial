student = {
    "name":"John",
    "age":30,
    "rollno":12,
    "year":2010
}

name = student["name"]
print("name :",name)

age = student.get("age")
print("age",age)

#key()
stud_key = student.keys()
print("stud_key :",stud_key)
print(type(stud_key))

#values
stud_value = student.values()
print("stud_value :",stud_value)
print(type(stud_value))

#items method
stud_items = student.items()
print("stud_items :",stud_items)
print("types :",type(stud_items))