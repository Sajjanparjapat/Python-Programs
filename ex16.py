from sys import argv

script, filename = argv
txt = open(filename)
print "This is the current content of the file : ", txt.read()
print
txt.close()
print "We're going to erase %s." %filename 
print "If you don't want that, hit CTRL+C. If you do want that, hit Return."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
txt ="\n" + line1 + "\n" + line2 + "\n" + line3
target.write(txt)

print "And finally , we close it."
target.close()

print "Opening file again for the reviewing the new content and the new content of the file is as below"
txt = open(filename)
print txt.read()

print "And again, closing this file."
txt.close()