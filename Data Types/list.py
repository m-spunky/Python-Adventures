# List Comprehension
a = [i for i in range(11) if i % 2 == 0] 
print(a)
[0, 2, 4, 6, 8, 10]

print(a[1:])
[2, 4, 6, 8, 10]

print(a[:1])
[0]

print(a[-1:])
[10]

print(a[:-1])
[0, 2, 4, 6, 8]

print(a[2:4])
[4, 6]

print(a[::-1])
[10, 8, 6, 4, 2, 0]

def m(n):
    print(n)

# list ( map ( FUNCTION , ARRAY ) )
list(map(m,[3,4,5,7]))
