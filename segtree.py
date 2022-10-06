# Python3 Code Addition
 
# limit for array size
N = 8
 
# Max size of tree
tree = [0] * (2 * N)
 
# function to build the tree
def build(arr) :
 
    # insert leaf nodes in tree
    for i in range(n) :
        tree[n + i] = arr[i]
     
    # build the tree by calculating parents
    for i in range(n - 1, 0, -1) :
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
 
# function to update a tree node
def updateTreeNode(p, value) :
     
    # set value at position p
    tree[p + n] = value
    p = p + n
     
    # move upward and update parents
    i = p
     
    while i > 1 :
         
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1

# function to get sum on interval [l, r)
def query(l, r) :
 
    res = 0
     
    # loop to find the sum in the range
    l += n
    r += n
     
    while l < r :
     
        if (l & 1) :
            res += tree[l]
            l += 1
     
        if (r & 1) :
            r -= 1
            res += tree[r]
             
        l >>= 1
        r >>= 1
     
    return res
 
# Driver Code
if __name__ == "__main__" :
 
    a = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12]
    N = len(a)
    tree = [0]*(2*N)
    n = len(a)
    build(a)
    print(tree)
    print(query(1, 3))
    
    
    updateTreeNode(2, 1)
    
    print(query(1, 3))