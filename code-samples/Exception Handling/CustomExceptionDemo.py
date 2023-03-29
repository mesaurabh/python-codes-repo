class SmallNumberException(Exception):
    """Raise when number is less than 10"""
    pass


class LargeNumberException(Exception):
    """Raise when number is greater than 100"""
    pass


try:
    number = int(input("Enter number between 10 & 100"))
    if number < 10:
        raise SmallNumberException("Number is less than 10")
    elif number > 100:
        raise LargeNumberException("Number is greater than 100")
except SmallNumberException:
    print("Number is less than 10, pls enter within 10 to 100")
except LargeNumberException:
    print("Number is greater than 100, pls enter within 10 to 100")


