
# this one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1 = %r ,arg2 = %r ." % (arg1, arg2)

def print_two_param(arg1, arg2):
	print "arg1 = %r ,arg2 = %r ." % (arg1, arg2)

def print_one(arg1):
	print "arg1 = %r ." % arg1

def print_none():
	print "nothing ."


print_two("hello", "world")
print_two_param("hello", "python")	
print_one("this is one")
print_none()