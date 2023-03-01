def add(number1, number2):
    result = number1 + number2
    print(f"Result = {result}")
    return result


def arithmetic(number1, number2):
    addition = number1 + number2
    sub = number1 - number2
    multiply = number1 * number2
    division = number1 / number2

    return addition, sub, multiply, division


if __name__ == '__main__':
    a, b, c, d = arithmetic(100, 50)
    print(f"addition result {a}")
    print(f"sub result {b}")
    print(f"multiplication result {c}")
    print(f"division result {d}")
    res2 = add(40, 60)
    res3 = add(55, 55)
