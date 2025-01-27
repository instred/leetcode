from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(set)
        for start, end in prerequisites:
            graph[start].add(end)

        canReach = [[False] * numCourses for _ in range(numCourses)]
        self.bfs(numCourses, graph, canReach)

        ans = []
        for q1, q2 in queries:
            ans.append(canReach[q1][q2])

        return ans

    def bfs(self, numCourses, graph, canReach):
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for adj in graph[node]:
                    if not canReach[i][adj]:
                        canReach[i][adj] = True
                        q.append(adj)
        


if __name__ == "__main__":
    sol = Solution()
    numCourses = 2  
    prerequisites = [[1,0]]  
    queries = [[0,1],[1,0]]  
    numCourses2 = 2  
    prerequisites2 = []  
    queries2 = [[1,0],[0,1]]  
    numCourses3 = 3  
    prerequisites3 = [[1,2],[1,0],[2,0]]  
    queries3 = [[1,0],[1,2]]
    print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))
    print(sol.checkIfPrerequisite(numCourses2, prerequisites2, queries2))
    print(sol.checkIfPrerequisite(numCourses3, prerequisites3, queries3))