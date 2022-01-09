def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)



# Should print the multiplication table shown below

# 1 2 3 

# 2 4 6 

# 3 6 9

# multiplication table logic breakdown

# Function Definiton: multiplication_table	|	parameter value: start, stop
# for loop	|	using range function starting from start and ending at stop+1
# for loop	|	using range function starting from start and ending at stop+1
# printing string x * y for for loop of y
# printing function for for loop of x

# puuting value of 1,3 in the function which means, start=1, stop=3