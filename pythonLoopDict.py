studentDict = {
    "firstName":"john",
    "lastName":"cena",
    "age":28
}

#
for x in studentDict:
    print(x)

for x in studentDict:
    print(studentDict[x])

print("---using key method ---")
for x in studentDict.keys():
    print(x)

print("--using values method---")
for x in studentDict.values():
    print(x)

print("using items method")
for x,y in studentDict.items():
    print(x,y)

 