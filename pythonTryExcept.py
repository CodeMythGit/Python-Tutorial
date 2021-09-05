'''
python exception
try - exception trowable code
except - exception handling mechanism
finally - close operation/imp task
'''
#multiple exception
try:
    print(2/2)
except NameError:
    print('x is not defined')
except:
    print("Exception occured")
else:
    print("No exception occured")

print("hello")

try:
    print("Hello friends")
except:
    print("Exception")
finally:
    print("inside finally block")

'''raise exception'''
x = 10
if x<15:
    raise Exception("Value is less than 15")