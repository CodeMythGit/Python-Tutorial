"values"
"hello world"

variable_name = "values"

name = "ABC"

# print(name)

#muliple line string  
#syntax triple quates """text"""
paragraph = """This is code myth youtube channel,
and here we are leaning programming   .
lang"""
# print(paragraph)

s = "hello world"
#string is an array in python
#index start in 0
print(s[10])

#string length
#len(variable_name)
text = "This is python"
print(len(text))


#check string is present in text or not
text = "this string contains abc"
print("ABC" in text) #True or False

print("other" not in text) 

#slicing 
#syntax 
#variable_name[start_pos:end_pos:step]
#variable_name[start_pos:end_pos]

s = "Hello world!"
print(s[0:5]) #Hello

print("---Slice from the start---")
print(s[:7])

print("---Slice to the end---")
print(s[3:])

print("--negative slicing--")
print(s[-5:-2])

name = "Rahul Dravid"
#slicing using step
print("slicing using step")
print(name[0:6:2])
print(name[::3])
