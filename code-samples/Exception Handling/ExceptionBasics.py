try:
    print(x)
except NameError:
    print("NameError Exception occured ...")
except:
    print("Some other exception apart from NameError has occured ... ")
