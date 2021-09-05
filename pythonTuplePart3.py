

#tuple -> list -> change -> tuple 
tuple1 = ("a","b","c","d","e")

tuple_list = list(tuple1)
print("type : ",type(tuple_list))

tuple_list.append("apple")
print("Updated list : ",tuple_list)

tuple1 = tuple(tuple_list)
print("type : ",type(tuple1))
print("updated tuple :",tuple1)

print("delete tuple")
del tuple1

print("Tuple 1 :",tuple1)



