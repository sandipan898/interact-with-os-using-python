# file operation

file = open("../areas.py")

#reads the first line
print(file.readline())

#reads the next line
print(file.readline())

# reads from the next line to end
print(file.read())

# closing the file 
file.close()

# open a file with "with" so we don't have to close it
with open("../areas.py") as file:
	print(file.read())
