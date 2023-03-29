textToWrite = " opening a file into append mode to verify the results"
fileToWrite = open("write_demo.txt", 'a')
fileToWrite.write(textToWrite)
print('Completed the file writing part')
fileToWrite.close()
