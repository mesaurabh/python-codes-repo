if __name__ == '__main__':
    # 20 , lambda function for adding 10 to a number
    x = lambda num: num + 10
    print(x(40))

    addition = lambda a, b, c: a + b + c
    print(addition(10, 11, 12))

    strconcat = lambda str1, str2, str3: str1 + " " + str2 + " " + str3
    print(strconcat('windows', 'unix', 'linux'))

    numberList = [-19, 20, 56, -87, 54, -67, 444, -786]

    positiveNumberList = list(filter(lambda number: number > 0, numberList))
    print("Positive numbers are : ", positiveNumberList)

    numList = [2, 4, 6, 8, 10]
    numSquare = list(map(lambda num: num * num, numList))
    print("Square of number in a list are : ", numSquare)

    nList = [5, 3, 9, 6, 18]
    sortedList = sorted(nList, reverse=True)
    print("Sorted list numbers are : ", sortedList)

    minNumber = min(nList)
    maxNumber = max(nList)

    print("Minimum number from list ", minNumber)
    print("Maximum number from list ", maxNumber)

    multiplicationResult = pow(4, 3, 5)  # --> ((4*4*4*4*4) % 3)
    print("pow() result ", multiplicationResult)

    num1 = 7.9657843
    roundedNumber = round(num1, 3)
    print("output of round() function ", roundedNumber)

    listSum = sum(nList)
    print("Sum of all the numbers in the list ", listSum)

