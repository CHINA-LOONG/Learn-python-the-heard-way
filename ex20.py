# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(_f_):
	print _f_.read()


def print_line(line,_f_):
	print _f_.readline(),

def rewind(_f_):
	_f_.seek(0)

file_data = open(input_file)


print "全部："

print_all(file_data)

print "分布式："
rewind(file_data)

print_line(1,file_data)
print_line(1,file_data)
print_line(1,file_data)