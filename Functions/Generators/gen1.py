def base(i):
    a = 20
    while a > i:
        # return something
        yield a + i

        # make changes for next round
        a = a + i

# Calling Generator
set = base(10)

# Printing all ITERATOR
# for i in range(100):
print(next(set))
print(next(set))

