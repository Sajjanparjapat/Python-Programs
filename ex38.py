ten_things = "Apple Orange Banana Light Sugar"
print ten_things
print "Wait this list is not complete please add more item to make it 10 items in the list."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Moon", "Google", "Facebook","Youtube","Automation"]

while len(stuff) !=10:
	next_element = more_stuff.pop()
	print "Adding %s" %next_element
	stuff.append(next_element)
	print "There are %d items in items." %len(stuff)
	
print stuff

print stuff[1]
print stuff[8]
print stuff[-1]

print stuff.pop()
print '_'.join(stuff)
print '#'.join(stuff[2:5])
print ''.join(stuff[2]+' & '+stuff[5])