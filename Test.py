from sys import argv
from os.path import exists

script, from_file, to_file = argv;

if (exists(from_file)):
	print "From file exist %s and reading content from the same.\n" %from_file

indata = open(from_file)
txt = indata.read()
print txt

todata = open(to_file, 'a')
todata.write(txt)
todata.write("\n")
indata.close()
todata.close()

print "Reading content from the Copied file.\n"
txt = open(to_file, 'r')
print txt.read()
txt.close()
