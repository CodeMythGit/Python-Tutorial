#what is set , property, built in method
#set are used to store muliple values/items in a single variable

#{} 
#property unordered unchangeable,unindexed 
firstSet = {"sachin","virat","dhoni"}
print("firstSet :",firstSet)

#unchangeable
firstSet.add("saurav")
print("Updated set :",firstSet)

#length of set -> len(variable_name)
print("length of firstSet : ",len(firstSet))

print("type :",type(firstSet))

set1 = ("a","b","c")
set2 = (1,2,3)
set3 = (True,False)

set4 = ("a",1,True,False)
print("set4 : ",set4)

#set using constructor
#syntax -> set((data_values))

set5 = set(("a","v","c"))
print("type of set5 is : ",type(set5))