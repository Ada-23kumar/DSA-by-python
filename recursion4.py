# write a recursion function to print first N even number

def printNeven(n:int):
    # if n == 0:
    #     return 1
    # printNeven(n - 1)
    # print(2 * n, end=" ")
    while n > 0:
        printNeven(n - 1)
        print(2 * n)
        return

printNeven(10)