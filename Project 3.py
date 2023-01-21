#Samad Khan

def retirement(amount, age, retireAge, rate, monthly, percentWithdraw):
	amount=10000
	rate=4.2/100
	percentWithdraw=4/100


	while amount > 0:
		amount= amount - rate - percentWithdraw
		years= years + 1

	return years

def main():
	# Prompt the user for the initial amount
	temp = input('What is the inital balance? ')
	balance = int(temp)
	
	# Prompt the user for the rate
	temp = input('What is the rate? ')
	rate = int(temp)
	
	temp = input('What is the percentWithdraw?')
	percentWithdraw = int(temp)

	temp = input('What is the Current Age')

	# calculate final 
	totalYears = retirement(amount, )
	print('At this rate your savings will last', totalYears, 'years.')
	
# call the main function to run the program
main()