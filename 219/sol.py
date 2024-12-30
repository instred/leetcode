from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        visited = {}
        for i, n in enumerate(nums):
            if n in visited:
                if i - visited[n] <= k:
                    return True
            visited[n] = i

        return False
    

 


if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    nums2 = [1,0,1,1]
    k2 = 1
    nums3 = [1,2,3,1,2,3]
    k3 = 2
    nums4 = [2,2]
    k4 = 3
    s = Solution()
    print(s.containsNearbyDuplicate(nums, k))
    print(s.containsNearbyDuplicate(nums2, k2))
    print(s.containsNearbyDuplicate(nums3, k3))
    print(s.containsNearbyDuplicate(nums4, k4))