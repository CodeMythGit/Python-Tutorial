#if logical_condition:
    #operation 1
#else:
    #operation 2

a = 20
b = 30
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")

#short if statement
if a<b:print("a is less than b")

#ternory operator
a = 10
b = 10
print("a is greater than b") if a>b else print("a is not greater than b")
#condition ? true:false

a = 20 
b = 30
c = 40
if a>b and b>c:
    print("a is greater than b and c")
else:
    print("Not true")

a = 40 
b = 30
c = 20
if a>b or c>b:
    print("a is greater than b and c")
else:
    print("Not true")

a = 10 
b = 30
c = 40
if a>b:
    print("a is greater than b")
elif b>c:
    print("b is greater than c")
else:
    print("Nothing is true")

#use of pass statement
a = 10
b = 20
if a>b:
    pass
