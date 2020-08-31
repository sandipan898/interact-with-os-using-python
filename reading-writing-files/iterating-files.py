with open("../areas.py") as file:
	for line in file:
		print(line.upper()) # adds a new line 

print("--------------------------------")
# removing new line character from the file
with open("../areas.py") as file:
	for line in file:
		print(line.strip().upper()) # adds a new line 

print("--------------------------------")
file =  open("../areas.py")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
