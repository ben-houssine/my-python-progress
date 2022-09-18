
#creating two arrays
numbers_1 = [1,2,3]
names_1 = ['name1','name2','name3']

#one way to display items of an array, one by one together:
displaying_option_1 = list(zip(numbers_1, names_1))
print(displaying_option_1)

print("")

#another way to display it:
#creating two arrays
numbers_2 = [1,2,3]
names_2= ['name1','name2','name3']

for val1, val2 in zip(numbers_2, names_2):
    print(val1,val2)

"""
Option one will have the following output:
[(1, 'name1'), (2, 'name2'), (3, 'name3')]

Option two will have this output:
1 name1
2 name2
3 name3
"""
