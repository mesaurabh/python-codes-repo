def countDigits(n):
    ans = 0
    while (n):
        ans = ans + 1
        n = n // 10
    return ans


num = 123456
print("Number of digits in the given number :", countDigits(num))
