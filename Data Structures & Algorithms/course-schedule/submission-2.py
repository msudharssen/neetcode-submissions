class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for i in range(numCourses):
            adjList[i]=list()
        for i, course in enumerate(prerequisites):
            adjList[course[0]].append(course[1])
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not adjList[course]:
                return True
            
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjList[course].clear()
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True