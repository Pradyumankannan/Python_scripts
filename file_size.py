import os

filename = 'test.txt' 

size = os.stat(filename).st_size

f = open(filename,"a+")
f.write(" " * 1024)
print(size)