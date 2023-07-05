memory = {}
def memorize(func):
	def base(num):
		if num not in memory:
			memory[num] = func(num)
			print('result saved in memory')
		else:
			print('returning result from saved memory')
		return memory[num]

	return base
	
@memorize
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

print(facto(5))

# directly coming from saved memory
print(facto(5)) 