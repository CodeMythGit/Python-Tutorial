class Error(Exception):
    pass

class ValueIsLessThanTarget(Error):
    pass

class ValueIsGreaterThanTarget(Error):
    pass

age = 18
while True:
    try:
        age_input = int(input("Enter a number: "))
        if age_input<age:
            raise ValueIsLessThanTarget
        elif age_input>age:
            raise ValueIsGreaterThanTarget
        break
    except ValueIsLessThanTarget:
        print("Entered age is less than expected age")
    except ValueIsGreaterThanTarget:
        print("Entered age is greater than expected age")
    
print("Congrats!!!!")
