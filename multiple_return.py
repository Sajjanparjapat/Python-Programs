def mymath(a,b):
	sum = a+b
	return sum,a-b,a*b,a/b,a*a,b*b,a%b
	
add,sub,multiply,divide,firstsquare,secondsquare,reminder=mymath(20,3)
print add, sub, multiply, divide, firstsquare, secondsquare, reminder