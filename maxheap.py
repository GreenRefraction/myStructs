from typing import Callable, Iterable
import math

class MaxHeap:
    class Node:
        left = None
        right = None
        def __init__(self, data) -> None:
            self.data = data

        def swap(self, child):
            temp = self.data
            self.data = child.data
            child.data = temp

        def check_invariant(self, child, key:Callable|None=None):
            if key is None:
                if self.data < child.data:
                    self.swap(child)
            else:
                if key(self.data) < key(child.data):
                    self.swap(child)

        def push(self, new_node, k, key:Callable|None=None):
            if k == 3:
                self.right = new_node
                self.check_invariant(self.right, key)
            elif k == 2:
                self.left = new_node
                self.check_invariant(self.left, key)
            elif k & 1:
                self.right.push(new_node, k >> 1, key)
                # check the heap invariant
                self.check_invariant(self.right, key)
            else:
                self.left.push(new_node, k >> 1, key)
                # check the heap invariant
                self.check_invariant(self.left, key)
        def __str__(self) -> str:
            return str(self.data)

    def __init__(self, iter:Iterable=None):
        self._root = None
        self._length = 0
        if iter is not None:
            for i in iter:
                self.push(i)


    def push(self, data, key=None):
        if self._length == 0:
            self._root = self.Node(data)
            self._length = 1
        else:
            new_node = self.Node(data)
            self._root.push(new_node, self._length+1, key)
            self._length += 1

    def pop(self):
        if self._length == 0:
            raise Exception("Empty Heap")
        elif self._length == 1:
            out = self._root.data
            self._root = None
            self._length -= 1
            return out
        out = self._root.data
        
        last_node = self._get_node(self._length, self._root)
        self._root.data = last_node.data
        # sift down
        k = self._length
        curr = self._root
        while k > 3:
            if k & 1:
                curr.check_invariant(curr.right)
                curr = curr.right
            else:
                curr.check_invariant(curr.left)
                curr = curr.left
            k >>= 1
        if k & 1:
            curr.right = None
        else:
            curr.left = None
        self._length -= 1
        return out

    def _get_node(self, k, curr:Node):
        if k == 2:
            return curr.left
        elif k == 3:
            return curr.right
        if k & 1:
            return self._get_node(k >> 1, curr.right)
        else:
            return self._get_node(k >> 1, curr.left)

    def top(self):
        return self._root.data

    def __str__(self) -> str:
        out = ""
        if self._length ==  0:
            return ""
        curr_layer = [self._root]
        next_layer = list()
        for i in range(int(math.log2(self._length)) + 1):
            next_layer = list()
            out  += " ".join(map(lambda d: str(d) if d is not None else "-", curr_layer)) + "\n"
            while len(curr_layer) > 0:
                curr = curr_layer.pop(0)
                if curr is not None:
                    next_layer.append(curr.left)
                    next_layer.append(curr.right)
            curr_layer = next_layer
        return out


if __name__ == '__main__':
    N = 21
    mheap = MaxHeap(range(N))
    for i in range(N):
        print(mheap.pop())
        print(mheap)
        input()
