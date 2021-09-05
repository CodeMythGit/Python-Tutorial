i = 1
while i<6:
    print(i)
    i+=1

#1. break statment
#2. continue stmt
#3. else stmt

#1. break stmt
print("--break stmt---")
i = 1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

print("---continue stmt---")
i = 1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#3. else stmt
print("else stmt")
i = 1
while i<6:
    print(i)
    if i==4:
        break
    i+=1
else:
    print("while loop ended")
    

