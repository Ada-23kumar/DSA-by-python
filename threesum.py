from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums.sort()
        self.print_sort(nums)
        length = len(nums)
        threeSet = set()

        for i in range(length - 2):  
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    threeSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1  
                else:
                    right -= 1  

        return list(threeSet)
    
    def print_sort(self, nums: List[int]):
        num = len(nums)
        for j in range(num):
            swap = False
            for i in range(num - j - 1):
                if(nums[i] > nums[i + 1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swap = True
            if not swap:
                break
        return nums
    
        
                    

    
if __name__ == "__main__":
    result = Solution()
    lst = [-1, 0, 1, 2, -1, -4]
    solution = result.threeSum(lst)
    print(solution)
    print(result.print_sort(lst))