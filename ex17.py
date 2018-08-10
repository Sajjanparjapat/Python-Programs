from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copy content from %s to %s" %(from_file, to_file)
print
in_file = open(from_file)
indata = in_file.read()
print indata
print
print "The input file is %d btyes long" %len(indata)
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit enter to continue, Press CTRL+C to abort"
raw_input()
out_file = open(to_file, 'a')
out_file.write(indata)
print "data has been copied"
out_file.close()
in_file.close()
print "Reading data from the copied file."
txt = open(to_file)
print 
print txt.read()
txt.close()

#file mode, w - first will truncate the existing data of the file and then  write the new data.
#file mode, a - will start writing  in the file on the last line of the file by default in case there is no position mentioned to be start writing.