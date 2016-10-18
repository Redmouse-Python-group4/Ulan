import os
from datetime import date

path = raw_input("Enter your path: ")
file = raw_input("Enter name of your file/directory: ")
s = os.listdir(path)
abspath = "%s\\%s"%(path, file)
for i in s:
	if i == file:
		print abspath
		print "Size: %s" %(os.stat(abspath).st_size)
		print "Creation time: %s" %(os.stat(abspath).st_ctime)
		print "Modification time: %s" %(os.stat(abspath).st_mtime)
