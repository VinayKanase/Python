language = 'Python'

# len function returns total length of string
print(len(language))

# Get each letter in word of String

letter = language[0]
print(letter)

# letters from 0 to 3rd index
letters = language[0:3]

print(letters)

# letters from 1 to last index
letters = language[1:]

print(letters)

#  Negative index starts counting from end

letter = language[-1]
print(letter)

# String methods

upperCaseLanguage = language.upper()

print(upperCaseLanguage)

lowerCaseLanguage = language.lower()

print(lowerCaseLanguage)

longString = "Lorem ipsum dolor sit amet consectetur adipisicing elit."

print(longString.find('amet'))
print(longString.replace('amet', 'AMET'))
