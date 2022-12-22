class Allocator:

    def __init__(self, n: int):
        self.arr=[0]*n
        self.n=n

    def allocate(self, size: int, mID: int) -> int:
        count=0
        index=-1
        for i in range(self.n-1,-1,-1):
            if(self.arr[i]==0):
                count+=1
                if(count>=size):
                    index=i
            else:
                count=0
        if(index==-1):
            return index
        for i in range(index,index+size):
            self.arr[i]=mID
        return index

    def free(self, mID: int) -> int:
        count=0
        for i in range(len(self.arr)):
            if self.arr[i]==mID:
                count+=1
                self.arr[i]=0
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)