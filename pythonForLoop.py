colorlist = ["red","orange","yellow"]
for x in colorlist:
    print(x)

name = "larry"
for s in name:
    print(s)

#break continue else
#1.break stmt
print("break stmt")
colorlist = ["red","orange","yellow"]
for color in colorlist:
    if color=="orange":
        break
    print(color)

print("continue stmt")
colorlist = ["red","orange","yellow","black","white"]
for color in colorlist:
    if color == "yellow":
        continue
    print(color)

#3. else stmt
print("else stmt")
colorlist = ["red","orange","yellow","black","white"]
for color in colorlist:
    print(color)
else:
    print("success")

#range(5)-> 0,1,2,3,4
for n in range(5):
    print(n)

#range(3,20)
for n in range(3,10):
    print(n)
print("----------increment by-----")
#range(start,end,increment_by)
for n in range(3,20,4):
    print(n)

list1 = ["a","b","c"]
list2 = [1,2,3]
for alpha in list1:
    for num in list2:
        print(alpha,num)

for color in colorlist:
    pass