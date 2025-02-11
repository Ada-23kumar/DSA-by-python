# write a recursion function to print first N natural number in reverse order

def reverse_natural_number(n:int):
    # if n == 0:
    #     return 1
    # print(n, end=", ")
    # reverse_natural_number(n - 1)
    while n > 0:
        print(n)
        reverse_natural_number(n - 1)
        return 


reverse_natural_number(10)