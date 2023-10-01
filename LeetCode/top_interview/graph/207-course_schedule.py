class Solution:
    def canFinish(self, numCourses, prerquisites):
        adj_list = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerquisites:
            adj_list[course].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)

            for pre in adj_list[course]:
                if not dfs(pre):
                    return False

            adj_list[course] = []
            visited.remove(course)

            return True

        for course in adj_list:
            if not dfs(course):
                return False

        return True

