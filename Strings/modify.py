str = "This Is a Demo String"

# print(str.find('SUBSTRING',START_INDEX,END_INDEX))
print(str.find('is',1,5))
# returns index of first occurence of substring


print(str.split('i'))
# ['Th', 's Is a Demo Str', 'ng']


# print(str.replace('STRING TO BE CHANGED','STRING UPDATED',COUNTER OF CHANGES))
print(str.replace('Demo','Not A Demo',1))
# This Is a Not A Demo String


print("This is a {} String".format('Demo'))
# This is a Demo String



list = ['Th', 's Is a Demo Str', 'ng']
print(''.join(list))
# Ths Is a Demo Strng