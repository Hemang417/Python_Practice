import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments) # Writes the sentence present in comments
  filesize = os.path.getsize(filename) # Gets the size of the file specified
  return(filesize)

print(create_python_script("program.py"))