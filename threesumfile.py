from threesum import Solution
solution = Solution()
ls = []
# num = int(input("Enter the size of array: "))
# print("Enter the element in the array")
# for i in range(num):
#     print(i, " ", end = "")
#     ls.append(int(input()))
# print(ls)
lst = [2, 1, 5, 7, 8, -1, -3, 4, 6, 0, -2, -5, -7, -8]
result = solution.threeSum(lst)
print(solution.print_sort(lst))
print(result)
