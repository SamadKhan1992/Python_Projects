#Samad Khan

def compareInvestments(balance, age, retireAge, rate, monthly1, monthly2):
	#define the paramitars of the function

	balance=1000
	age=20
	retireAge=70
	rate= (4.2/100/12)
	monthly1=100
	monthly2=200


	print('  Year  |  Balance')
	print('========|=========')

	# annual calculation
	for year in range(numYears):
	
		# monthly calculation
		for month in range(12):
			interest = balance * rate
			balance1 = balance + interest + monthly1
			balance2 = balance + interest + monthly2
		# end inner for loop
		
		# print the results for the year
		print('{0:^7} | {1:8.2f}'.format(year+1, balance))
def main():
	#print out heading for function
	print('\t\t\tRetirement Calculator')
	print('\t\tDetermine how much money you could save')
	print('\t\tby saving X amount a month and')
	print('\t\tputting the money in an interest-bearing account')
	print()
	
	#getting the amount
	temp = input('What is your current balance?')
	Currentamount = int(temp)
	temp = input('How much will you invest the first time? ')
	invest1 = float(temp)
	temp = input('How much will you invest the second time')
	invest2 = float(temp)
	temp = input('What interest rate can you earn? ')
	rate = float(temp)
	temp = input('Over how many years should the calculation run? ')
	years = int(temp)
	
	# 
	compareInvestments(balance, age, retireAge, rate, monthly1, monthly2)
	
# end main

main()