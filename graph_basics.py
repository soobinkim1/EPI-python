"""
Graph: Overview
- Degree: number of edges connected to a node.
    - Indegree: number of edges pointing to a node
    - Outdegree: number of edges pointing out of a node.
- Can use to represent:
    - Implication - if B is true, then A is true (B -> A)
    - Locations
    - Preservation of certain orders
- Types of Graphs
    - Tree: No edge ever points back. Directed graph with no cycle.
    - Path: List of vertices such that (vi, vi+1) is in E for all i
        - Simple Path: Repeats no vertices.
        - Cycle: Start & end in same node.
        - Simple Cycle: Repeats no vertices but first vertex is also the last.
- Edge Cases
    - Nodes with no edges - Issue for traversing a graph.
    - Cycles - Issue for traversing a graph. => Track visited.
    - Loops - Node is its own neighbor. => Filter where node is its own neighbor.
"""
graph = { 'A': ['B', 'C'], 'B': ['C'], 'C': ['D'], 'D': ['C']}

"""
Graph: Topological Sort (for Acyclic Graphs)

- Topological Sort: Ordered list created from a graph. For every directed edge <u, v>, u precedes v in the ordering.

- Topological Sort Algorithm => O(V^2 + E)
    - Build hash table for { vertex: [in-degree edges]}. => O(E).
    - Find a vertex w/ indegree = 0. => since search V array V times, O(V^2).  
        - That vertex can come first, since it will precede all other vertices.
        - If no such vertex, the graph is cyclical.  => There is no topological sort.
    - Remove such vertex & output to the result array => O(V).
    - Remove incoming edge for all Vs that removed V was pointing to => O(E)
    - Repeat until graph is empty.

=> Can we find vertices with indegree 0 w/o searching entire in-degree array, which takes O(V^2)?

- Topological Sort Algorithm => O(E + V), O(V)
    - Store each v's indegrees in an array. => O(E)
    - Maintain a queue of v with indegree 0. => O(V)
    - Remove v with indegree 0. => O(V)
    - While removing incoming edge for all Vs that removed V was pointing to, enqueue any vertex whose in-degree is now zero. => O(E)
    - Time: O(E+V)
    - Space: O(V)

"""
def topological_sort(graph): 



"""
!Graph: Find the judge.
- In a graph of N, find a node that has indegree = N - 1 & outdegree = 0
"""
def find_judge(graph):
    return 

"""
Graph: Path 
- Path Length: # edges on a path.
- Path Cost: Sum of costs of each edge.

- BFS => O(E+V)
    - Explore all nodes one step away, then explore all nodes two steps away, etc.
    - ex: rippling out from the starting point.
    - Better for minimum cost path.
    - ex: queue = [[A], [A, B], [A, C], [A, B, C], [A, B, D]]
    - Applications: route optimization; lowest-cost travel; fastest paths.
- DFS
    - Explores all paths down one path, until backing up and trying a new one.
    - Must track visited.
- Dijkstra Algorithm: shortest path in weighted graphs w/o negative weights.
    - Greedy algorithm - Makes an irrevocable decision without checking future consequences.
    - Each vertex stores a cost for path from source.
    - Expand from the vertex with the least path cost seen so far. 
"""
def djikstra(graph, start, end):
    


def shortest_path_bfs(graph, start, end):
    # if start is not in graph, terminate
    # create a queue, containing a path array for each path taken => O()
    # - deque() allows for fast pop from left and right
    from collections import deque
    if start not in graph.keys():
        return None
    q = deque()
    q.append([start]) # => O(V)
    visited = [] # If it has already been visited, then the path that already visited the node is shorter than the subsequent path.  More efficient by ruling out paths that clearly take longer.  More efficient if "visited" is a property on a node.
    visited.append(start)
    while len(q) > 0:
        new_path = q.popleft()
        if new_path[-1] == end:
            return len(new_path) - 1 # return length - 1
        if len(graph[new_path[-1]]) > 0: # are there any neighbors? => O(E)
            for n in graph[new_path[-1]]:
                if n not in visited: # has it been visited yet?
                    q.append(new_path[:] + [n])
    return -1

# print(shortest_path_bfs(graph, 'A', 'B'))
# print(shortest_path_bfs(graph, 'A', 'C'))
# print(shortest_path_bfs(graph, 'A', 'D'))

def check_path(graph, start, end):
    # while queue is not empty, traverse one by one
    # if already visited 
    # if queue.popleft() == end, return True
    # else, queue.extend(graph[queue.popleft()])
    from collections import deque
    q = deque()
    q.extend(graph[start])
    visited = [] # Track visited to avoid visiting node that has already been visited
    while len(q) > 0: # Falsey if q is empty
        curNode = q.popleft()
        if curNode == end:
            return True
        visited.append(curNode)
        q.extend([node for node in graph[curNode] if node not in visited])
    return False
    # time: O(V + E), with E edges followed & V vertices added to queue
    # space: O(V - 1), for storing max # of neighbors in a queue

#print('check_path', check_path(graph, 'A', 'B'))
# print('check_path', check_path(graph, 'B', 'A'))

graph = { 'A': ['B', 'C'], 'B': ['C'], 'C': ['D'], 'D': ['C']}

def shortest_path_dfs(graph, start, end, path = []):
    # if start is not in graph, return no path
    # if start == end, return len(path)
    # otherwise, visit the neighbor, until the neighbor's path includes "end" or has no further neighbors to explore

    if start not in graph.keys():
        return None # RETURN None since the path is illegal

    path = path + [start] # list concatenation must be explicitly written out
    if start == end:
        return len(path) - 1 # RETURN distance since the path was achieved

    shortest = None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = shortest_path_dfs(graph, neighbor, end, path) # RETURN the completed distance or None
            if new_path: # IF distance was returned, check whether to update distance
                if not shortest or new_path < shortest:
                    shortest = new_path
    return shortest # RETURN the completed distance or None

# print(shortest_path_dfs(graph, 'A', 'B'))
# print(shortest_path_dfs(graph, 'A', 'C'))
# print(shortest_path_dfs(graph, 'A', 'D'))
# print('A' in test_graph.keys())


"""
!Graph - Bidirectional Search
- Simultaneously start BFS from start and BFS from finish.
- Path found upon the BFSs colliding in midpoint.
"""
graph = { 'A': ['B', 'C'], 'B': ['C'], 'C': ['D'], 'D': ['C']}

def shortest_path_bi(graph, start, end):
    return

"""
Graph: Legal Coloring
- In a graph where each node has max D neighbors, assign one of D+1 colors to each node such that node has a color that differs from all its neighbors.
- Since a node has at most D neighbors, there is always one additional color that has not yet been assigned.
"""
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def legal_coloring(graph, colors):

    # loop through each node
    # for each node, create a list of colors have not yet been used by neighbors
    # take the first of such colors
    # Each node has at most D neighbors, and there are D+1 colors. So there's at least one color that has not been taken by the neighbors. 
    
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible with a loop %s'%node.label)
        illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break

    return 0
    # time: O(N+M), for N in # of nodes + M for # edges
    # space: O(D), for # edges
