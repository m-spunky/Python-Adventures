def base(i):
    # set value of variable only once (When Generator is called)
    a,b = 0,1
    
    # Block of Code run when next(gen)
    while a<i:
        # return value of variable (a) at time of that next(gen) call 
        yield a

        # make changes for next round
        a,b = b , a+b

# Calling Generator
set = base(60)

# Printing all ITERATOR
for i in range(50):
    print(next(set))

