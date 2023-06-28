# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
f = open("Python-Adventures/Input-Outputs/demofile.txt", "r")
for x in f:
  print(x)
f.close()

# "a" or "w" - Append - Opens a file for appending, creates the file if it does not exist
f = open("demofile1.txt", "a")
f.write("Now the file has more content!")
f.close()

# "x" - Create - Creates the specified file, returns an error if the file exists
f = open("demofile2.txt", "x")
f.write("Now the file has more content!")
f.close()

# For Removing File
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# For Removing Folder
import os
os.rmdir("myfolder") 


