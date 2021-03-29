import random
from colored import fg, bg, attr

# copy this into myCode.py if you need to restart.

def colors ():
	# change the colors
	print ('%s%s ListoMatic !!! %s' % (fg('white'), bg('yellow'), attr('reset')))
	print("\n")



def listoMatic():
	# comment
	myList = []


	# comment
	x = 10


	# comment
	while x > 0:
		# comment
		randomNum = random.randint(1,2)
		
		# comment
		myList.append(randomNum)

		# comment
		x = x - 1
		print(x, "debug")
	
	print("\n")
	print (myList, "%s%s The list of random numbers %s" % (fg('green'), bg('purple_3'), attr('reset')))

	lengthIs = len(myList) 

	
	print("\n")
	print(f'There are {lengthIs} hats in the shop.')

