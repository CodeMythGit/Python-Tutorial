#local scope and global scope

#named variables
x = 20

def myFunc():
    # x = 10
    global x
    x = 30
    print(x)

print(x)
myFunc()
print(x)