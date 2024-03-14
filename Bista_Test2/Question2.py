#Question_2 : Pythagorean triplets

def pythagorean_Triplets(limits) : 
	c, m = 0, 2
	triplet_list = []

	while c < limits : 
		
		for n in range(1, m) : 
			
			a = m * m - n * n 
			b = 2 * m * n 
			c = m * m + n * n 

			if c > limits : 
				break
			
			triplet_list.append((a,b,c))
	
		m = m + 1
	print(triplet_list)
    #return triplet_list

limit = 31
result = pythagorean_Triplets(limit) 






