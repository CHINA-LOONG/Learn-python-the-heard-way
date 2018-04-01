from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping file from %s to %s." % (from_file, to_file)

in_file = open(from_file)

in_data = in_file.read()

print "The input file is %d bytes long." % len(in_data)

print "Does the out_file has exists? %r ." % exists(to_file)


out_file = open(to_file, 'w')

out_file.write(in_data)

out_file.close()
in_file.close()



