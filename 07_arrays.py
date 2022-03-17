# Arrays/Lists

languages = ["HTML", "CSS", "JS"]

print(languages)

print(languages[0:2])

print(languages[1])


alotZeros = [0] * 20

print(alotZeros)


# Unpacking

lang1, lang2, lang3 = languages

markupLang, *other = languages

print(lang1, lang2, lang3)
print(markupLang)
print(other)

# Add new element at end of array

languages.append('Python')

# Add new element at given position

languages.insert(0, 'C')

print(languages)

# Removes last Item from array/list

languages.pop()

print(languages)


# Tupple
# with Tupple we cannot modify data only read it.
letters = ('a', 'b', 'c', 'd', 'e', 'f')

print(letters)


# Sets
# does not allow repetation of elements
setOfIntegers = {-4, -3, -2, -1, 0, 1, 2, 3, 4, -4}

print(setOfIntegers)


# List in Python

nameList = list("Vinay Kanse")
print(nameList)

# Range List

list1 = list(range(0, 101))
list2 = list(range(0, 101, 5))

print(list1)
print(list2)
