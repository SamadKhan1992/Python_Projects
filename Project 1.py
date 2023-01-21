#Samad Khan

"""A simulation of a calcuator for how long 
it will take you to pay off your loans"""

def comparePayoff(amount, rate, monthly1, monthly2):
	"""
	Simulate the how long needed to repay college loans
	
	Parameters:
		
		amount - amount of loan
		
		rate - monthly rate of Loan

		Monthly - Payment per month
	
	Returns:  The number of years that it will take to pay off loan
	
	"""
	#The inital Balance
	Inital_Balance=60000
	Nominal_Annual_Percentage_Rate=5
	Monthly1=500
	Monthly2=750

	years=0
	while amount >0:
		Nominal_Annual_Percentage_Rate = amount * (5/100/12)
		Monthly1=Monthly1 - Nominal_Annual_Percentage_Rate
		Monthly2=Monthly2 - Nominal_Annual_Percentage_Rate
		Inital_Balance1= Inital_Balance - Monthly1
		Inital_Balance2= Inital_Balance - Monthly2
		years = years + 1

	return years

def main():
	#Propmt the user for the Loan Amount
	temp = input("What is the Loan Amount?")
	amount= int(temp)

	#Prompt the user for Nominal Rate
	temp = input("What is the Annual Intrest")
	Nominal_Annual_Percentage_Rate = int(temp)

	#Prompt Payment 1
	temp = input("What is your first Monthly Payment")
	Monthly1 = int(temp)

	#Prompt Payment 2
	temp = input("What is your second Monthly Payment")
	Monthly2 = int(temp)


	#calculate final amount
	totalYears = comparePayoff(Inital_Balance1, Monthly1)
	print('Paying $500 it will take', totalYears, 'years to pay off your loan')

	totalYears2= comparePayoff(Inital_Balance2, Monthly2)
	print('Paying $750 it will take', totalYears2, 'years to pay off your loan')

main()