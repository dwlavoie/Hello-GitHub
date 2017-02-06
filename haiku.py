#make a Haiku in the target filename
from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want to do that, exit. (Ctrl+C)"
print "If you want to do that, hit RETURN."

raw_input("?")
print "Opening File..."
target = open(filename,'w')

print "Truncating File..."
target.truncate()

print "Please input three lines"

line1 = raw_input("5 Syllable Line: ")
line2 = raw_input("7 Syllable Line: ")
line3 = raw_input("5 Syllable Line: ")

print "Writing to file %r" % filename
target.write("%r\n%r\n%r\n" % (line1,line2,line3))

print "Closing file %r" % filename
target.close()
