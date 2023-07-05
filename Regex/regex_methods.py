import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# ['ai', 'ai']


txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start()) 
# The first white-space character is located in position: 3



txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
# ['The', 'rain', 'in', 'Spain']



txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# ['The', 'rain in Spain']


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# The9rain9in Spain


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# (12, 17)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# The rain in Spain


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Spain