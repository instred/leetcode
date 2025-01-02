from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            csum = numbers[i] + numbers[j]
            if csum > target:
                j -= 1
            elif csum < target:
                i += 1
            else:
                return [i+1, j+1]
    

if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    numbers2 = [2,3,4]
    target2 = 6
    numbers3 = [-1,0]
    target3 = -1
    print(sol.twoSum(numbers, target))
    print(sol.twoSum(numbers2, target2))
    print(sol.twoSum(numbers3, target3))