i = 0

numbers = []

while i < 10:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    break
    print "Numbers new:", numbers
    print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
    print num
