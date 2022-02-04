import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename,'w') as file: 
    """This line is to create a file in the current directory"""
    pass
  timestamp = os.path.getmtime(filename)
  c=datetime.datetime.fromtimestamp(timestamp)
  # Convert the timestamp into a readable format, then into a string
 
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(c.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd