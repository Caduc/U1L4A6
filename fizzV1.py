

import sys

#  print "The name of this script is {}".format(sys.argv[0])
#  print "User supplied {} arguments at run time".format(len(sys.argv))
#  
#  for arg in sys.argv[1:]:
#    print arg

top_num = 100
num = 0

while num < top_num:
	num  += 1
	if num%3 == 0 and num%5 == 0:
		fb = 'fizzbuzz'
	elif num%3 == 0:
		fb = 'fizz'
	elif num%5 == 0:
		fb = 'buzz'
	else:
		fb = str(num)

	print "{:>2d}".format(num) + ': ' + fb
		
