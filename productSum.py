'''Product sum of a special array is the sum of its elements and returns its productSum. A specialarray is a non empty array that contains either integers or other special arrays. The productSum of special array is the sum of its elements where special array inside it should be 
summed themselves and multiplied by their level of depth. For example the productSum of [x,y] is x+y, the productSum of [x,[y,z]] is x + 2y + 2z.'''  
def productSum(array,multiplier = 1):
	sum = 0
	for i in array:
		if type(i) is list:
			sum += productSum(i,multiplier+1)
		else:
			sum += i
	return sum * multiplier
		
productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) 
