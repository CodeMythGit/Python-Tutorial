set1 = {"a","b","c","d"}
set2 = {"c","f","g"}

#update method
# set1.update(set2)
# print(set1)

# print("example using string")
# set1 = {"a","b","c","d"}
# strValue = "apple"
# set1.update(strValue)
# print(set1)

print("example using list")
set1 = {"a","b","c","d"}
listValue = ["a","b","f","g"]
set1.update(listValue)
print(set1)

print("example using tuple")
set1 = {"a","b","c","d"}
tupleValue =("b","d","e")
set1.update(tupleValue)
print(set1)
