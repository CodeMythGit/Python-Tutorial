tuple1 = ("apple","banana","mango","kiwi")

#for loop
#syntax : 
#for variable in iterable_var_name:
    # do something

for x in tuple1:
    print("value : ",x)

#range and length method 
""" print("print using range and index method")
for x in range(len(tuple1)):
    print(tuple1[x])

print("print using while loop")
i = 0
while i <len(tuple1):
    print(tuple1[i])
    i+=1 """

#tuple join
t1 = (1,2,3,4)
t2 = (2,3,5)
t3 = t1 +t2
print(t3)

t3 = t1 *2
print("t3 using multiply : ",t3)
