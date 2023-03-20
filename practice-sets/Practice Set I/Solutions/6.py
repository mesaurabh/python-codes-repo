n = int(input("Enter number"))
res = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    res = res + num
print("Sum of first ", n, "numbers is: ", res)
