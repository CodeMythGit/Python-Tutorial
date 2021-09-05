'''
open - file open

4 mode 
r - read mode
a - append (content) - exception
w - overwrite - (old content with new content)
x - create

t = text
b  =binary

rt - read text

open - parameter,mode
'''
# path : full path
# f = open("Python Beginner\demo.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("Python Beginner\demo.txt")
# print(f.read())
# f.close()

""" f = open("Python Beginner\demo.txt","w")
f.write("File content is overwritten successfully!!")
f.close() """

""" f = open("Python Beginner\demo.txt","a")
f.write("\nFile content is appended successfully!!")
f.close() """

import os
if os.path.exists("Python Beginner\demo.txt"):
    os.remove("Python Beginner\demo.txt")
    print("File deleted successfully!!")
else:
    print("File does not exist")


