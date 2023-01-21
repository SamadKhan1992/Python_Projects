# How long until 10 tribbles 
# become a million tribbles?

# initialize count 
count = 10
hour = 0
while count < 1000000:
	count = count + int(count*0.5)
	hour = hour + 1
	print (hour, count)

print (hour)