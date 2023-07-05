# item == {key : value}

# Dictionary Comprehension
keys = [1,2,3,4]
values = ['monday','tuesday','wednesday','thursday']
dict1 = { key:value for (key,value) in zip(keys, values)} 


dict2 = dict1.copy()
print(dict2)
{1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday'}  


dict1.clear()
print(dict1)
{}


print(dict2.get(1))
'monday' 

print(dict2.items())
[(1, 'monday'), (2, 'tuesday'), (3, 'wednesday'), (4, 'thursday')]

print(dict2.keys())
([1, 2, 3, 4])  

dict2.pop(4)
print(dict2)
{1: 'monday', 2: 'tuesday', 3: 'wednesday'}

dict2.popitem()
print(dict2)
{1: 'monday', 2: 'tuesday'}

dict2.update({3: "Wednesday"})
print(dict2)
{1: 'monday', 2: 'tuesday', 3: 'Wednesday'}

print(dict2.values())
(['monday', 'tuesday', 'Wednesday'])



