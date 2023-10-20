ipsum_file = open("files/ipsum.txt")


# for line in ipsum_file:
#     print(line.rstrip())

# ipsum_file.seek(100)#puting the cursor at pos 100

lines = ipsum_file.readlines()
print(lines)
