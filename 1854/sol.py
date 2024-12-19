from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        dates = []
        for b, d in logs:
            dates.append((b,1))
            dates.append((d,-1))

        dates.sort()

        population = max_population = max_year = 0
        for y, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = y
        
        return max_year


if __name__ == "__main__":
    logs = [[1993,1999],[2000,2010]]
    logs2 = [[1950,1961],[1960,1971],[1970,1981]]
    logs3 = [[2000,2001]]
    s = Solution()
    print(s.maximumPopulation(logs))
    print(s.maximumPopulation(logs2))
    print(s.maximumPopulation(logs3))