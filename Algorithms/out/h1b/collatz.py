class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    def push(self,value):
        self.heap.append(value)
        curr = len(self.heap)-1
        
        while curr > 0 and self.heap[(curr-1)//2] < self.heap[curr]:
            p = (curr-1)//2
            self.heap[curr],self.heap[p] = self.heap[p], self.heap[curr]
            curr = p
        

    def pop(self):
        if not self.heap:
            return 0,0,0
        
        max = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            i = 0
            self.heap[0] = last

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                
                if left >= len(self.heap):
                    break

                larger = right if right < len(self.heap) and self.heap[right] > self.heap[left] else left

                if self.heap[i] >= self.heap[larger]:
                    break

                self.heap[i],self.heap[larger] = self.heap[larger],self.heap[i]
                i = larger

        return max



def collat(num):
    length = 1
    best = 0
    
    while num != 1:
        if num % 2 == 0:
            num //=2
        else:
            num = 3*num+1
        length += 1
        best = max(best,num)
    return length,best



if __name__ == "__main__":
    heap = MaxHeap()
    for num in range(1,10000000+1):
        length, best = collat(num)
        heap.push((length, num, best))
    for i in range(10):
        length, num, best = heap.pop()
        print(f"{i+1}. Collatz sequence for {num}: {length} {best}") 
