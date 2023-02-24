if __name__ == '__main__':

    programmingLangsTuple = ("Python", "Java", "Scala", "Go-Lang", "Ruby")
    print(f"Printing Tuple --> {programmingLangsTuple}")

    # tuple can contain different data types:
    tuple1 = (1, "Pune", "Maharashtra", 411033)
    print(f"0th element in Tuple :: {tuple1[0]}")
    print(f"1st element in Tuple :: {tuple1[1]}")
    print(f"2nd element in Tuple :: {tuple1[2]}")
    print(f"3rd element in Tuple :: {tuple1[3]}")

    fruits = ("apple", "banana", "cherry")

    (green, yellow, red) = fruits

    print(green)
    print(yellow)
    print(red)

    # Join 2 tuples
    tuple2 = programmingLangsTuple + fruits
    print(tuple2)




