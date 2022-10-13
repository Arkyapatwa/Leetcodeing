#User function Template for python3

class Solution:
    def rat(self,r,c,m,n,visited,path,res):
        if r<0 or c<0 or r>=n or c>=n or visited[r][c] or m[r][c]==0:
            return 
        
        if r==n-1 and c==n-1:
            res.append(path)
            return 
        
        for dir in self.dic.keys():
            x=dir[0]
            y=dir[1]
            visited[r][c]=1
            self.rat(r+x,c+y,m,n,visited,path+self.dic[dir],res)
            visited[r][c]=0
        
    def findPath(self, m, n):
        # code here
        self.dic={(1,0):"D",
            (0,1):"R",
            (-1,0):"U",
            (0,-1):"L"
        }
        res=[]
        visited=[[0 for _ in range(n)] for a in range(n)]
        if self.rat(0,0,m,n,visited,"",res)
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends