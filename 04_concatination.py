firstName = "Vinay"
lastName = "Kanse"

fullName = firstName + " " + lastName

print(fullName)

# Other way instead of concatination
#! NOTE: This works with python3 only
greeting = f"Hello {firstName} {lastName}"

print(greeting)

# Quotes inside strings
# ? using escape characters (\) Eg: \" \n, \t

quote = "Someone said \"Time is more important than money, money once gone can be earned back.\""

print(quote)

quote = 'Someone said "Time is more important than money, money once gone can be earned back."'


# Three quote text.

information = """                                    
                                               Title
Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates temporibus quo quam voluptas voluptatibus, id necessitatibus sapiente repellendus sequi magni. Quos eveniet quae impedit nam quod commodi vel culpa ratione reprehenderit sint? Perspiciatis, fugit. A culpa incidunt saepe laudantium!
"""
print(information)
