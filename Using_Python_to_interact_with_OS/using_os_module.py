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