class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for i in range(numCourses):
            adjList[i]=list()
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visited = set()
        cycle = set()
        ans = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for cor in adjList[crs]:
                if not dfs(cor):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            ans.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return ans