import os,sys
sname=input("enter source file name to copy:")
if os.path.isfile(sname):
	s=open(sname,'r')
else:
	print(sname,"does not exist")
	sys.exit()
tname=input("enter new file name:")
if os.path.isfile(tname):
	print(tname,"exist,use new file name only")
	sys.exit()
else:
	t=open(tname,'w')
str=s.read()
t.write(str)
print("file copied sucessfully")
print("\n contents in sourse file are:\n")
print(str)
s.close()
t.close()
print("\n contents in new file are:\n")
t=open(tname,'r')
st=t.read()
print(st)
t.close()
