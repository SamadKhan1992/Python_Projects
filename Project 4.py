#Samad Khan
# copy the following two lines into any
# program that you write that will work with files
"""Program is to find and replace certain parts of the message into making another message to be sent"""
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# open said file, read the file
def getFileData(filename):

#Make into a list
	list=[]
	file = open(os.path.join(__location__,filename), 'r')

# attach each line to the list	
	for line in file:
		list.append(line)

#closes said file and returns the list	
	file.close()
	return list

def TestScores(filename):
	listofScore=[]
	for score in midterms:
		Range = ''  # Get range
		Number = ''  #get number
		Percent = '' # get percentage

		# process the line.  Use an index into the line to access each character
		index = 0
		ch = score[index]  # Title
		while ch != ' ':
				title = title + ch
				index = index + 1
				ch = score[index]


#used to find the Max of the numbers
def findMax(numbers):
	max= numbers[0]
	index = 1
	while index < len (numbers):
		if numbers[index] > max:
			max = numbers[index]
		index = index + 1
	return max


#used to find the min of the numbers

def findMin(numbers):
	min= numbers[0]
	index = 1
	while index < len (numbers):
		if numbers[index] < min:
			min = numbers[index]
		index = index + 1
	return min

# used to find the average

def average(numbers):
	n = len ( numbers )
	sum = 0
	for number in numbers:
		sum = sum + int(number)
		
	average = sum/n
	return average

#print out the table for the bottom part
def table(numbers):
	
	print('\n\nRange of score\t\tNumber\tPercent')
	print('='*50)
	






def main():

	numbers = getFileData('midterms.txt')
	biggest = findMax(numbers)
	smallest= findMin(numbers)
	avg = average(numbers)
	

	print('\t\t\tAnalysis of Test Scores')
	print('\n\t\tThe high score is:', biggest )
	print('\n\t\tThe low score is:', smallest )
	print('\n\t\tThe average is', avg )
	table(numbers)






main()


