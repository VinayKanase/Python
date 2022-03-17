fruit = "apple"

fruit2 = fruit

print(fruit2)

fruit2 = "mango"

print(fruit2)


fruits = ['apple', 'banana', 'kiwi']

fruits2 = fruits

fruits2.append('mango')

print(fruits2)
print(fruits)

#! Here, we can see list changed in fruits2 also changed list in fruits it is because fruits and fruits2 are referenced same
# ? For solving this problem instead of equalizing fruits2 and fruits we can create copy of fruits to fruits2

fruits2 = fruits.copy()

fruits2.append('grapes')
print(fruits2)
print(fruits)


# MUTABLE VALUES
# bool, int, floats, tuples, strings

# UNMUTABLE VALUES
# lists, sets, dict
