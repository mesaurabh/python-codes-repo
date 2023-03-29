try:
    x = "Welcome to Python Training"
    print(x)
    testFile = open('test.txt', 'r')
    # print(testFile.read())
    fileAsString = testFile.read()
    fileContent = testFile.readlines()
    testFile.close()
except FileNotFoundError:
    print("Unable to locate input file ...")
except NameError:
    print("Variable x is not defined ...")
except:
    print("Something went wrong ...")
