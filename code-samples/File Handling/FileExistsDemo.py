import os.path

fileName = "test3.txt"

isFilePreesnt = os.path.isfile(fileName)
fileExists = os.path.exists(fileName)

print(fileExists)
