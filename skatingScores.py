# skating scores - a program to determine a skater's
# score using the 'trimmed mean'.

# csc 140

# The program works as follows:
#  1) The user is prompted to enter 9 scores in the range of 1 - 10.
#     The scores represent the evaluation of a skater's performance
#     given by each of 9 judges.
#  
#     The scores are validated as they are entered.  The scores are
#     stored in a list named 'scores'.
#  
#  2) The scores are passed as an argument to a function named 
#     'trimmedAverage'.  This function uses two other functions,
#     'findHighest' and 'findLowest', to determine which two elements
#     to 'trim' from the calculation of the average.  trimmedAverage
#     then calculates and returns the average of the remaining 7 scores.
#  
#  3) The main function prints the skater's score.

def trimmedAverage(scores):
	""" Find the average of the entries in the list, after eliminating
	    the highest and the lowest entry
		
		Parameter:  a list of integer values representing scores
		
		Returns:  a float value representing the 'trimmed mean' of the entries
		          in the list
				  
		Uses:   This function uses the findHighest and findLowest functions
		        to determine which scores to eliminate
	"""
	# put the code for the trimmedAverage function here
	n = len ( scores )
	sum = 0
	for number in scores:
		sum = sum + number - min - max
		
	average= sum/n
	return average

	
def findHighest(scores):
	""" Find and return the highest value in the list of values that is passed in
	
	    Parameter: a list of integer values
		
		Returns:  The highest value in the list
	"""
	# put the code for the findHighest function here

	max= numbers[0]
	index = 1
	while index < len (numbers):
		if numbers[index] > max:
			max = numbers[index]
		index = index + 1
	return max

	
def findLowest(scores):
	""" Find and return the lowest value in the list of values that is passed in
	
	    Parameter:  a list of integer values
		
		Returns:  The highest value in the list
	"""
	# put the code for the findLowest function here

	max= numbers[0]
	index = 1
	while index < len (numbers):
		if numbers[index] < max:
			max = numbers[index]
		index = index + 1
	return max

	
def main():
	""" Communicate with the user and call the supporting functions to determine 
	    the trimmed mean of the scores
	
		Parameters:  None
		
		Returns:  Nothing
	"""
	
	# Create an empty list
	scores = []
	
	# Prompt the user to enter 9 scores.  Validate that the scores are between 0 and 10, inclusive
	
	for count in range(1,10):
		temp = input('Scores are between 0 and 10, inclusive.  Enter score ' + str(count) + ': ')
		score = int(temp)
		
		# validate
		while score < 0 or score > 10:
			print('Error: ' + str(score) + ' is invalid.')
			temp = input('Scores are between 0 and 10, inclusive.  Enter score ' + str(count) + ': ')
			score = int(temp)
			
		# put score in the list
		scores.append(score)
		
	# at this point, the user has entered 9 scores.  Determine and display the trimmed average
	trAverage = trimmedAverage(scores)
	print('The score for this skater is:', trAverage)
	
# run the program
main()