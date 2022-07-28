import os 

f = open("extension.txt", "r")
op = f.read()
#put ur paths
for i in op:
	src = path1
	dst = path2
	dst = dst+i
	copyfile(src,dst)