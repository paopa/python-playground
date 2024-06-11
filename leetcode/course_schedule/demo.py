from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for coruse, prerequisite in prerequisites:
            graph[prerequisite].append(coruse)

        # print(graph)

        # visited node
        visited = set()

        def dfs(course):
            if course in visited:
                return False  # cycle detected
            if graph[course] == []:
                return True  # no prerequisites for this course

            visited.add(course)
            for c in graph[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


obj = Solution()

graph = [[1, 0]]
output = obj.canFinish(2, graph)
assert output == True

graph = [[1, 0], [0, 1]]
output = obj.canFinish(2, graph)
assert output == False

graph = [[1, 0], [2, 0], [3, 1], [4, 1], [4, 3]]
output = obj.canFinish(5, graph)
assert output == True
