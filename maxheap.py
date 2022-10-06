import math
import sys
 
class MaxHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.arr = [None] * (self.maxsize + 1)
 
    def swap(self, fpos, spos):
        self.arr[fpos], self.arr[spos] = (self.arr[spos], self.arr[fpos])

    def _sift_up(self, k):
        while k > 1:
            if self.arr[k] > self.arr[k >> 1]:
                self.swap(k, k >> 1)
            k >>= 1
    
    def _sift_down(self, curr):
        parent = curr >> 1
        if parent == 0: return
        self._sift_down(parent)
        if self.arr[curr] > self.arr[parent]:
            self.swap(curr, parent)
        if self.arr[curr^1] is not None and self.arr[curr^1] > self.arr[parent]:
            self.swap(curr^1, parent)
        

    def push(self, element):
        self.size += 1
        self.arr[self.size] = element
        self._sift_up(self.size)
 
    def pop(self):
        if self.size == 1:
            popped = self.arr[1]
            self.arr[1] = None
            self.size = 0
        else:
            popped = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            self._sift_down(self.size)
        return popped

    def __str__(self) -> str:
        if self.size == 0:
            return ""
        out = ""
        curr_layer = [1]
        for k in range(int(math.log2(self.size)) + 1):
            out += " ".join(map(lambda i: str(self.arr[i]) if i <= self.size else "-", curr_layer)) + "\n"
            next_layer = list()
            for i in curr_layer:
                left = i << 1
                right = left  + 1
                next_layer.append(left)
                next_layer.append(right)
            curr_layer = next_layer
        return out
    def __len__(self):
        return self.size
# Driver Code
if __name__ == "__main__":    
    heap = MaxHeap(15)
    N = 10
    for i in range(N):
        heap.push(i)
    for i in range(N):
        print(heap.pop())
    
    