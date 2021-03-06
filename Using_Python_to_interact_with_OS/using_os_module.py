import os
"""This is to remove the file from the path"""
os.remove("file_name")
"""This is to rename the file from te hold_name to the new_name"""
os.rename("old_name", "new_name")
"""os.path.exists gives boolean value in return as in: True or False"""
os.path.exists("file_name") #if true the file exists
                            #if false the file does not exist

os.path.getsize("file_name") # This returns file-size of the file in bytes

os.path.getmtime("file_name")# returns a timestamp of the last modified 
"""To convert this timestamp into date and time, we need to convert the folowwing using datetime module: 
datetime.datetime.fromtimestamp(timestamp) the variable timestamp consists of the timestamp we get from os.path.getmtime"""

os.path.abspath("file_name")#returns absolute path of the file

os.getcwd() # to get the current working directory

os.mkdir("directory_name") # to create a directory with the name of file_name
os.chdir("directory_name") # to change the directories and move to the specified directory_name
os.rmdir("directiory_name")# removes an directory only when the directory is empty
os.listdir("directory_name") # lists the contents inside a directory
