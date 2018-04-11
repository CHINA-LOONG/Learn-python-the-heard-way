

hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weight = [1,2,3,4]




the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type : %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

for i in xrange(1,10):
	elements.append(i)

elements = range(1,100)

for i in elements:
	print "Elements was:%d" % i
