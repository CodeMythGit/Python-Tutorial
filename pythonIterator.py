mylist = ["apple","mango","banana","kiwi"]
#next and iter

# myiter = iter(mylist)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# name = "Sachin"
# myiter = iter(name)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# for x in name:
#     print(x)

# print("on list")
# for x in mylist:
#     print(x)

class CustomeIterator:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num<=10:
            num = self.num
            self.num+=1
            return num
        else:
            raise StopIteration

c = CustomeIterator()
myiter = iter(c)

#use of stopiteration keyword
for x in myiter:
    print(x)

