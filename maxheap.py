import sys

 
class MaxHeap:
    def __init__(self, iter=None, key=None):
        self.size = 0
        if key is None:
            key = lambda i: i
        self.key = key
        self.arr:list = [None]
        if iter is not None:
            for i in iter:
                self.push(i)
    
    def swap(self, fpos, spos):
        self.arr[fpos], self.arr[spos] = (self.arr[spos], self.arr[fpos])

    def _sift_up(self, k):
        while k > 1:
            parent = k >> 1
            if self.key(self.arr[k]) > self.key(self.arr[parent]):
                self.swap(k, parent)
            else:
                break
            k = parent

    def _sift_down(self):
        k = 1
        while k <= self.size:
            left = k << 1
            right = left + 1
            parent = k >> 1
            if parent > 0 and self.key(self.arr[parent]) < self.key(self.arr[k]):
                self.swap(parent, k)
            if right <= self.size:
                if self.key(self.arr[left]) > self.key(self.arr[right]):
                    k = left
                else:
                    k = right
            else:
                k = left

    def push(self, element):
        self.size += 1
        self.arr.append(element)
        self._sift_up(self.size)
 
    def pop(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            popped = self.arr.pop()
            self.size = 0
        else:
            popped = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr.pop()
            self.size -= 1
            self._sift_down()
        return popped
    
    def top(self):
        return self.arr[1]

    def __str__(self) -> str:
        if self.size == 0:
            return ""
        out = ""
        curr_layer = [1]
        depth = 0
        k = self.size
        while k > 0:
            depth += 1
            k >>= 1
        for k in range(depth):
            out += " ".join(map(lambda i: str(self.key(self.arr[i])) if i <= self.size else "-", curr_layer)) + "\n"
            #out += " ".join(map(lambda i: str(self.arr[i]) if i <= self.size else "-", curr_layer)) + "\n"
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
    
    def _check_health(self, i=1):
        
        left = i << 1
        right = left + 1
        if left <= self.size:
            assert self.key(self.arr[i]) >= self.key(self.arr[left])
            self._check_health(left)
        if right <= self.size:
            assert self.key(self.arr[i]) >= self.key(self.arr[right])
            self._check_health(right)
# Driver Code
if __name__ == "__main__":
    for i in range(20, 100):
        heap = MaxHeap(range(i))
        print(heap)