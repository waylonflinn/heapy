An priority queue built with an in-place modifiable binary heap.

Operations have the following algorithmic complexities:

* `pop` - `O(log(n))`
* `push` - `O(log(n))` (average: `O(1)`)

Useful for:

* Dijkstra's shortest path algorithm
* A*
* Rolling median

## Examples
The following is an example implementation of Dijkstra's algorithm, a method
for finding the shortest path in a weighted graph. The heap-based
priority queue reduces the complexity of the basic algorithm from `O(n^2)`
to `O(m*log(n))`, for `n` nodes and `m` edges.


```python
from heapy import pqueue

def dijkstra(G, r):
	'''Find the shortest paths from a given node in a weighted graph
		to every other (connected) node.
	'''

    todo = pqueue() # this is the heap-based priority queue

    distance = {} # distances to all nodes on shortest paths
    parents = {} # parent pointers for all items on known shortest paths

    todo.push((r, 0)) # alternate syntax: todo[r] = 0

    n = None

    while todo: # automatically checks `len(todo) > 0`
        p = n
        (n, d) = todo.pop() # get the minimum element; O(log(n))


        distance[n] = d # shortest distance
        parents[n] = p # parent in minimum path spanning tree

        # update position of children in priority queue, if less
        children = G.get(n, {})
        for (c, w) in children.items():
            if c not in distance and (c not in todo or d + w < todo[c]):

                todo.push((c, d + w)) # will update, if already in the queue

    return distance
```
