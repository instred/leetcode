from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, idx = stack.pop()
                ans[idx] = i-idx
            stack.append((t, i))
                
        return ans
            
            


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    temperatures2 = [30,40,50,60]
    temperatures3 = [30,60,90]
    print(sol.dailyTemperatures(temperatures))
    print(sol.dailyTemperatures(temperatures2))
    print(sol.dailyTemperatures(temperatures3))