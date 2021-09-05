# name = "Rahul"
# # age = 50
# # s = "My name is "+name+" and I am "+age +" years old"
# # print(s)

# #single formatter
# #syntax
# # {}.format(value)
# s = "My name is {}"
# print(s.format(name))

# s = "Your one time password(OTP) is {}"
# otp = 4434
# print(s.format(otp))

text = "Dear {}, your otp is {}"
name = "Sachin"
otp = 5567
print(text.format(name,otp))

#position based formatter

name = "Sachin"
otp = 5567
print("Dear {1}, your otp is {0}".format(2345,"Suraj"))

#keyword based formatter
print("Dear {name}, your age is {age}".format(age=30,name="Arun"))

#f string
#syntax 
#f""
name = "Rahul"
age = 40
print(f"My name is {name} and i am {age} years old")



