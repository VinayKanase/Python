file = open("frontend.txt", "r")
# .readable - checks if file is readable
# .read - reads whole file
# .readline - reads line of a file
# .readlines - creates an array/list of lines
if file.readable():
    # print(file.read())
    # print(file.readline())
    print(file.readlines())
file.close()
