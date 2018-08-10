def print_two(*args):
	arg1, arg2 = args
	print "arg1 : %s, arg2 : %s" %(arg1,arg2)
	
def print_twoagain(arg1, arg2):
	print "arg1 : %s, arg2 : %s" %(arg1, arg2)
	
def print_one(arg1):
	print "arg1 : %s" %(arg1)
	
def print_nothing():
	print "This method is empty."
	
print_two("Sajjan","Alok")
print_twoagain("Sajjan","Varun")
print_one("Alok")
print_nothing()