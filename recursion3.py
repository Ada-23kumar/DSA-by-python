# write a recirsion function to print first N odd natural number
def printNodd(n):
    # if n== 0:
    #     return 1
    # printNodd(n-1)
    # print(2 * n - 1, end = ", ")
    while n > 0:
        printNodd(n - 1)
        print(2 * n - 1)
        return

printNodd(10)