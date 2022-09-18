
#creating two arrays
numbers = [1,2,3]
names = ['name1','name2','name3']

#one way to display items of an array, one by one together:
displaying_option_1 = list(zip(numbers, names))
print(displaying_option_1)
print("")

#another way to display it:
for val1, val2 in zip(numbers, names):
    print(val1,val2)

"""
1st output:
[(1, 'name1'), (2, 'name2'), (3, 'name3')]

2nd output:
1 name1
2 name2
3 name3
"""
