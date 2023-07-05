# WITHOUT DECORATOR
def algeb(x): 
    def adder(y):
        return x+y

    def subtractor(y):
        return x-y
    
    if x > 10:
        return adder
    else:
        return subtractor

# add_15 = algeb(x)  
add_15 = algeb(15) 
sub_15 = algeb(5)

# res = add_15(y)
res1 = add_15(10)
res2 = sub_15(10)

print(res1)
print(res2)


# WITH DECORATOR
def algeb(func):
	def base(*args, **kwargs):
		function = func(*args, **kwargs)
		return function
	return base

@algeb
def sum(a, b):
	return a + b

@algeb
def sub(a,b):
    return a - b

print(sum(5,10))
print(sub(5,10))

# similar as algeb(sum(5,10))