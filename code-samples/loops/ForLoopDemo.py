languages = ["python", "java", "scala"]

for lang in reversed(languages):
    print(lang)

for x in "oracle":
    print(x)

for x in languages:
    if x == "java":
        break
    print(x)

#range() function

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)
