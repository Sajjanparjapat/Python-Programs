def add(a,b):
	print "Adding %f + %f" %(a,b)
	return a+b
	
def sub(a,b):
	print "Subtracting %f - %f" %(a,b)
	return a-b

a =	float(raw_input("Enter the value of a: "))
b = float(raw_input("Enter the value of b: "))
print add(a,b)
print sub(a,b)