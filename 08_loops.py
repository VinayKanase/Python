# For loop

languages = ["C", "C++", "HTML", "CSS", "JS", "PYTHON"]


for language in languages:
    print("Language: " + language)


# for loop of numbers

for i in range(0, 21):
    print("Number: " + str(i))

# for loop with string

name = "Vinay Kanse"

for letter in name:
    print("Letter: " + letter)

# While loop

count = 0
while count <= 10:
    print("Repeated")
    count += 1

    if(count == 6):
        print("Count is 14 now")

# break - breaks the loop
# continue - skips one loop
