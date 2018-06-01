

def add(a, b):
    print "Adding %d +%d" % (a, b)
    return a + b


age = add(10, 5)


what = add(100, add(age, 5))

print "result:%d" % what
