# Open a file in write mode and write some text
#with open("testfile.txt", "w") as file:
 #   file.write("Hello, this is a test file.\n")
  #  file.write("Python is fun!\n")

# Open the same file in read mode and display the content
#with open("testfile.txt", "r") as file:
 #   content = file.read()
  #  print("File Content:\n", content)


with open("testfile.txt", "w") as file:
    file.write("Hello this is a test file. \n")
    file.write("Python is fun! \n")

with open("testfile.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)    