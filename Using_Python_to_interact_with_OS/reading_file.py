"""Here the file_name is the name of the file if the file is in the same directory or you can also enter
the absolute path of where the file is present"""
file = open("file_name")

"""This print function consists of a reaedline function which reads line from the file"""
print(file.readline())
"""When executed again like this, this readline function moves to the next line of the file"""
print(file.readline())

