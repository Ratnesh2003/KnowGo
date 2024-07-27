def get_smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def update_range_lazy(tree, lazy, node, start, end, l, r):
    if lazy[node] != 1:
        tree[node] = tree[node] // lazy[node]
        if start != end:
            lazy[node*2] *= lazy[node]
            lazy[node*2+1] *= lazy[node]
        lazy[node] = 1
    if start > r or end < l:
        return
    if start >= l and end <= r:
        tree[node] = tree[node] // get_smallest_prime_factor(tree[node])
        if start != end:
            lazy[node*2] *= get_smallest_prime_factor(tree[node])
            lazy[node*2+1] *= get_smallest_prime_factor(tree[node])
        return
    mid = (start + end) // 2
    update_range_lazy(tree, lazy, node*2, start, mid, l, r)
    update_range_lazy(tree, lazy, node*2+1, mid+1, end, l, r)
    tree[node] = tree[node*2] + tree[node*2+1]

def query_range(tree, lazy, node, start, end, l, r):
    if start > r or end < l:
        return 0
    if lazy[node] != 1:
        tree[node] = tree[node] // lazy[node]
        if start != end:
            lazy[node*2] *= lazy[node]
            lazy[node*2+1] *= lazy[node]
        lazy[node] = 1
    if start >= l and end <= r:
        return tree[node]
    mid = (start + end) // 2
    p1 = query_range(tree, lazy, node*2, start, mid, l, r)
    p2 = query_range(tree, lazy, node*2+1, mid+1, end, l, r)
    return p1 + p2

def update_index(tree, node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    if idx <= mid:
        update_index(tree, node*2, start, mid, idx, value)
    else:
        update_index(tree, node*2+1, mid+1, end, idx, value)
    tree[node] = tree[node*2] + tree[node*2+1]

def build_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    build_tree(arr, tree, node*2, start, mid)
    build_tree(arr, tree, node*2+1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]

def Divisor_Queries(N, Q, a, queries):
    tree = [0] * (4 * N)
    lazy = [1] * (4 * N)
    build_tree(a, tree, 1, 0, N-1)
    results = []
    for query in queries:
        if query[0] == 1:
            update_range_lazy(tree, lazy, 1, 0, N-1, query[1]-1, query[2]-1)
        elif query[0] == 2:
            results.append(query_range(tree, lazy, 1, 0, N-1, query[1]-1, query[2]-1))
        elif query[0] == 3:
            update_index(tree, 1, 0, N-1, query[1]-1, query[2])
    return results

# Example usage:
N = 10
Q = 9
a = [10, 9, 10, 10, 9, 9, 10, 9, 10, 10]
queries = [
    [1, 7, 8],
    [3, 1, 10],
    [3, 3, 10],
    [3, 4, 10],
    [3, 5, 10],
    [2, 8, 8],
    [2, 8, 8],
    [2, 7, 10],
]
print(Divisor_Queries(N, Q, a, queries))
