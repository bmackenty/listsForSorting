# This program is used to generate a rather large list of random numbers.
# This program creates an ordered and unordered list
# The list is then used for computer science students to 
# apply their understanding of standard searches and sorts. 


# the line below imports the random library, which enables us to use lots of functions with random.
import random
# the line below imports the time library, which enables us to use lots of functions with time
import time

# we need to time our program, so we are going to set the start time
start_time = time.time()

myList = []
numberToFind = 7000000000

def unsortedList():
	# this function 
	for i in range(0,50000):
		# the line line below simply appends a random number between 0 and 9,999,999 into our list
		myList.append(random.randrange(1,9999999))
	# the line below inserts our target number in a random location in our list. 	
	myList.insert(random.randint(0,9999),numberToFind)
	return myList


def sortedList():
	# this function 
	for i in range(0,50000):
		# the line line below simply appends a random number between 0 and 9,999,999 into our list
		myList.append(i)
	return myList


# this is where we call the functions to make our lists
# uncomment out the lines you 

# unsortedList()
# sortedList()



# =========================================================
# Your different sorting algorithms will go under this line
# =========================================================
















# =========================================================
# Your different sorting algorithms will go above this line
# =========================================================


# the lines below are used only for debugging. 
# print(myList)	
# The line below should print true if our target exists in our list. 	
# print(numberToFind in myList)

# print the execution time
print("--- %s seconds ---" % (time.time() - start_time))


# references
#
# I am grateful to stackoverflow for the code for timing a python program: 
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
