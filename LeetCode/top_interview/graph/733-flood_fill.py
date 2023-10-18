class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        org = image[sr][sc]
        visited = set()
        def dfs(r,c):
            if (
                    (r,c) in visited or 
                    (r < 0 or c < 0) or
                    (r == rows or c == cols) or
                    image[r][c] != org
                ):
                return
            image[r][c] = color
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr,sc)
        return image


#revised on 18-10-2023
class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        visited = set()
        org = image[sr][sc]
        def dfs(r,c):
            if (r >= rows or c >= cols or 
                r < 0 or c < 0 or 
                (r,c) in visited or 
                image[r][c] != org
                ):
                return
            visited.add((r,c))
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr,sc)
        return image


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2
s = Solution()
print(s.floodFill(image, sr,sc,color))
