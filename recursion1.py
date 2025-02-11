# write a recursive function to print first N natural number
def natural_number(n):
    if n == -1:
        return 0
    natural_number(n - 1)
    print(n, end=", ")

natural_number(10)