# Translates string to numbers

# Each letter is numbered from 1 to 26
# First is length of string then a zero and followed by string
# Example a is 1, b is 2 and so on....

# This is case insensitive


# Eg:
# String: A, a Value: 101
# String: Vinay Value: 5022914125
alphabets = "abcdefghijklmnopqrstuvwxyz"


def translate(string):
    strToNum = str(len(string))
    strToNum += '0'
    for letter in string:
        for i in range(len(alphabets)):
            if(letter.lower() == alphabets[i]):
                strToNum += str(i+1)

    return int(strToNum)


print(translate(input("Enter string: ")))
