"""Suppose we have some input data describing a graph of relationships between parents and children over multiple families and generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2    4           30
 \ /   /  \           \
  3   5    9  15      16
   \ / \    \ /
    6   7   12


Sample input/output (pseudodata):

pairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]


Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.


Output may be in any order:

findNodesWithZeroAndOneParents(pairs) => [
  [1, 2, 4, 15, 30],   // Individuals with zero parents
  [5, 7, 9, 16]        // Individuals with exactly one parent
]

Complexity Analysis variables:

n: number of pairs in the input"""

pairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]

# BFS Solution
def bfs_solution():
    adj_list = {}
    for src, dst in pairs:
        if src not in adj_list:
            adj_list[src] = []
        if dst not in adj_list:
            adj_list[dst] = []
        adj_list[src].append(dst)

    print(adj_list)
    freqs = {}
    for obj in adj_list:
        for item in adj_list[obj]:
            freqs[item] = freqs.get(item, 0) + 1

    print(freqs)

    # one parent:


# Brute Force - Non-Graph Solution
def set_and_counts(pairs):
    """
    Time Complexity: O(n)
    Memory Complexity: O(n)
    """

    # find all zero children first
    children = {pair[0] for pair in pairs}
    parents = {pair[1] for pair in pairs}

    # Create zero parent set
    zero_parent_set = children - children.intersection(parents)
    # convert to list
    zero_parent = list(zero_parent_set)

    # Get frequency of one parent elements
    parents_freq = {}
    for pair in pairs:
        parents_freq[str(pair[1])] = parents_freq.get(str(pair[1]), 0) + 1

    one_parent = []
    for k, v in parents_freq.items():
        if v == 1:
            one_parent.append(int(k))

    print(zero_parent)
    print(one_parent)
    return zero_parent, one_parent



if __name__ == "__main__":

    # brute force solution
    #set_and_counts(pairs)
    bfs_solution()
