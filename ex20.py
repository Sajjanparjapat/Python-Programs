from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)

def print_line(linenumber,f):
	print linenumber, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now Let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

currentline = 1
print_line(currentline,current_file)

currentline = currentline + 1
print_line(currentline,current_file)

currentline = currentline + 1
print_line(currentline,current_file)