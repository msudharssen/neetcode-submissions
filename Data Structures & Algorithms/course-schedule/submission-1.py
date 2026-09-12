class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        info = defaultdict(list)
        visited = set()

        for item in prerequisites:
            info[item[0]].append(item[1])
        
        def dfs(course):
            if course in visited:
                return False  
            if len(info[course])==0:
                return True 
            
            visited.add(course)
            for numb in info[course]:
                if not dfs(numb):
                    return False
            visited.remove(course)
            info[course].clear()
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True