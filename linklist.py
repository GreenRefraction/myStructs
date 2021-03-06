from typing import Iterable

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next:Node = None
        self.prev:Node = None
    
    def __del__(self) -> None:
        l = self.prev if self.prev is not None else None
        r = self.next if self.next is not None else None
        if l is not None:
            l.next = r
        if r is not None:
            r.prev = l
        
        
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self, iterable:Iterable=None) -> None:
        self._length = 0
        self.head:Node = None
        self.tail:Node = None
        if iterable is not None:
            for data in iterable:
                self.push_back(data)
    
    def push_back(self, data):
        node = Node(data)
        if self._length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._length += 1

    def push_front(self, data):
        node = Node(data)
        if self._length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._length += 1
    
    def pop_front(self):
        if self._length == 0:
            return None
        elif self._length == 1:
            data = self.head.data
            self.tail = None
            self.head = None
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        self._length -= 1
        return data
    
    def pop_back(self):
        if self._length == 0:
            return None
        elif self._length == 1:
            data = self.tail.data
            self.tail = None
            self.head = None
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        self._length -= 1
        return data

    def get_node(self, key) -> Node:
        if key >= self._length or key < -self._length:
            raise IndexError("Index out of range")
        if key >= 0:
            node = self.head
            for i in range(key):
                node = node.next
            return node
        else:
            node = self.tail
            for i in range(-1, key, -1):
                node = node.prev
            return node
    
    def values(self):
        if self._length == 0:
            return []
        node = self.head
        for i in range(self._length):
            yield node.data
            node = node.next
    
    def __len__(self) -> int:
        return self._length

    def __getitem__(self, key):
        if type(key) is slice:
            start = 0 if key.start is None else key.start
            stop = self._length - 1 if key.start is None else key.stop % self._length
            step = 1 if key.step is None else key.step
            
            out = LinkedList()
            s = self.get_node(key.start)
            for i in range(start, stop, step):
                if s is None: break
                out.push_back(s.data)
                for j in range(abs(step)):
                    s = s.next if step > 0 else s.prev
                    if s is None: break
            return out
        else:
            return self.get_node(key).data

    def __setitem__(self, key, val):
        if key >= self._length or key < -self._length:
            raise IndexError("Index out of range")
        if key >= 0:
            node = self.head
            for i in range(key):
                node = node.next
            node.data = val
        else:
            node = self.tail
            for i in range(-1, key, -1):
                node = node.prev
            node.data = val

    def __delitem__(self, key):
        if key >= self._length or key < -self._length:
            raise IndexError()
        if key >= 0:
            node = self.head
            for i in range(key):
                node = node.next
        else:
            node = self.tail
            for i in range(-1, key, -1):
                node = node.prev
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l
        self._length -= 1
    
    def __iter__(self):
        node = self.head
        for i in range(self._length):
            yield node
            node = node.next
    
    def __list__(self) -> list:
        out = list()
        s = self.head
        while s is not None:
            out.append(s.data)
            s = s.next
        return out

    def __str__(self) -> str:
        return str(self.__list__())


if __name__ == '__main__':
    LinkedList()
    a = [1, 2, 3, 4, 5]
    a = LinkedList(a)
    
    print("Access tests")
    assert str(a) == '[1, 2, 3, 4, 5]'
    assert a[0] == 1
    assert a[2] == 3
    assert a[-1] == 5
    assert type(a[0:2]) is LinkedList
    assert str(a[0:3]) == '[1, 2, 3]'
    
    a.push_back(6)
    print(a)
    a = LinkedList([1])
    print(a.pop_back())
    print(a.pop_back())
    a.push_back(3)
    print(a.head.data)

    print("delete test")
    a = list(range(10))
    print(a)
    del a[3]
    print(a)
    a = LinkedList(range(10))
    print(a)
    t = a[3]
    del t
    print(a)
    a = list(range(10))
    print(a)
    del a[3:5]
    print(a)
