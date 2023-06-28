str = "This Is a Demo String"

print(str[0])
# T

[print(x,end='') for x in str]
# This Is a Demo String

print("\nDemo" in str)
# Returns True if it is present in String 


# substring = str[start:end]
subs1 = str[0:2]
# bydefault start = 0
subs2 = str[:2]
subs3 = str[2:]
print(subs1)
print(subs2)
print(subs3)
# Th
# Th

# substring = str[(-)end:(-)rev_end]
subs1 = str[-3:-1]
# bydefault start = 0
subs2 = str[-2:]
subs3 = str[:-2]
print(subs1)
print(subs2)
print(subs3)
# in
# ng
# This Is a Demo Stri

