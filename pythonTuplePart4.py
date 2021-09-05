
#packing and unpacking in tuple
tuple1 = ("a","b",1,2,3,"c") #packing

#syntax : 
(var1,var2) = ("a","b")
# print("var1 :",var1)
# print("var2 :",var2)

tuple1 = ("apple","mango","banana")
(red,green,yellow) = tuple1
# print("red :",red)
# print("green :",green)
# print("yellow :",yellow)

# tuple1 = ("apple","mango","cherry","kiwi","banana")
# use * sign
# (red,*green,yellow) = tuple1
# print("red :",red)
# print("green :",green)
# print("type of green : ",type(green))
# print("yellow :",yellow)

tuple1 = ("apple","mango","cherry","kiwi","banana")
(red,green,*yellow) = tuple1
# print("red :",red)
# print("green :",green)
# print("type of green : ",type(green))
# print("yellow :",yellow)
# print("type of green : ",type(yellow))

#count and index built in method of tuple
tuple2 = ("1","a","b","c","d","a","b")

#count syntax -> var_name.count(values)
# print("Total a in tuple2 : ",tuple2.count("a"))
# print("Total b in tuple2 : ",tuple2.count("b"))
# print("Total f in tuple2 : ",tuple2.count("f"))

#index - > to get the index position use index method
#index method syntax -> var_name.index(value) var_name.index(value,start_index,end_index)
print("index of a in tuple2 : ",tuple2.index("a"))
print("index of a in tuple2 : ",tuple2.index("a",2,6))

# print("index of a in tuple2 : ",tuple2.index("a",6,20))
print("index of a in tuple2 : ",tuple2.index("a",4,20))




