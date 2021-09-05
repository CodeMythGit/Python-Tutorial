#1. creating a function
def my_function():
    print("first function in python")

#2. calling  a function
my_function()

def print_name_func(name):
    print("My name is :"+name)

print_name_func("Larry")

#3. arguments and parameters

def add(a,b):
    print(a+b)

add(10,5)

def func_arb(*name):
    print(name[0]+" : "+name[1])

func_arb("larry","25")

#keyword key = value
def keyword_func(color1,color2,color3):
    print(color1+" : "+color2+" : "+color3)

keyword_func(color2="red",color1="orange",color3="yellow")

def keyword_arg_func(**kargs):
    print(kargs["color1"])
keyword_arg_func(color2="red",color1="orange",color3="yellow")

def function1(num = 10):
    print(num)

function1(3)
function1()
function1(20)

list1 = ["apple","mango","banana"]
def list_function(list_value):
    for item in list_value:
        print(item)

list_function(list1)

#return function
def ret_func(a,b):
    return a+b;

print(ret_func(10,11))