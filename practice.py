with open("example.txt", "r") as file:
    content = file.read()
    print(content)
  
-----------------------------

with open("example.txt", "w") as file:
    file.write("Hello, World!\nThis is a file handling example.")
----------------------------

with open("example.txt", "a") as file:
    file.write("\nThis line was added later.")
---------------------------

file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()
------------------------
with open("example.txt", "r+") as file:
    content = file.read()
    print(content)
    file.write("\nNew content added.")

-------------------------
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)



