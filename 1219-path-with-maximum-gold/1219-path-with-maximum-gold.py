class Solution:
    def dfs(self,grid,x,y,count,row,col,visited):
        if x<0 or y<0 or x>=row or y>=col or not grid[x][y]:
            return 
        if grid[x][y]==0 or visited[x][y]:
            return
            
        count+=grid[x][y]
        self.res=max(count,self.res)
        visited[x][y]=True
        
        self.dfs(grid,x+1,y,count,row,col,visited)
        self.dfs(grid,x,y+1,count,row,col,visited)
        self.dfs(grid,x-1,y,count,row,col,visited)
        self.dfs(grid,x,y-1,count,row,col,visited)
        
        visited[x][y]=False
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[[False for _ in range(col)] for _ in range(row)]
        self.res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    self.dfs(grid,i,j,0,row,col,visited)
        return self.res