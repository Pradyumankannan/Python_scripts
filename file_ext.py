import os

from shutil import copyfile
import pandas as pd

url = 'https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01'
dfs = pd.read_html(url)
print(dfs[0]["Extension"])

#put ur paths
with open("Extension.txt","a") as o:
	for i in dfs[0]["Extension"]:
		l = i.split(", ")
		for j in l:
			o.write(j + ",")
			src = path1
			dst = path2
			dst = dst+j
			copyfile(src,dst)
