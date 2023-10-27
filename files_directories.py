from pathlib import Path

path = Path("packages")  # existing path
createPath = Path("Emails")  # creating path
print(path.exists())
print(createPath.mkdir())  # create a folder
print(createPath.rmdir())  # remove a folder

# search for files and folders
currentPath = Path()
for file in currentPath.glob("*.*"):
    print(file)
# print(currentPath.glob("*.py"))
