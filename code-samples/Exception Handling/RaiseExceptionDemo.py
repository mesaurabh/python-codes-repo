# We initialise one variable as x, expecting a positive number

x = -99
if x < 0:
    raise Exception("Negative numbers are not allowed")
else:
    print(f"Positive number value in x = {x}")
