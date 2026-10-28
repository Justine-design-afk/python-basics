# function methods

with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")

with open("temp.txt", "r") as file:
    content=file.read()
    print(content)




