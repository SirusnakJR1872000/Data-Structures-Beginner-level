from collections import deque

# now we will initialize a graph node for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

# now lets define a empty dictionary to store the adjacency list
adjlist = {}

# now we will run the loop over each pair of source and destination in the graph
for src, dst in edges:
    # we have to check if src or dst are there or not in adjacency list
    if src not in adjlist:
        adjlist[src] = []
    if dst not in adjlist:
        adjlist[dst] = []
    # now we can add the destination node to the source node
    adjlist[src].append(dst)

# now lets count the path using dfs
def dfs(node, target, adjlist, visit):
    # if the nod is already visited
    if node in visit:
        return 0
    if node == target:
        return 1
    
    # we will set the initial count to 0 to keep the track of valid paths
    count = 0
    # we will add the node to the visited
    visit.add(node)
    # now the loop will iterate through all the neighbors of the current node 
    for neighbor in adjlist[node]:
        # and we recursively call the function if we find the correct path
        count += dfs(neighbor, target, adjlist, visit)
    visit.remove(node)

    return count

# now lets see the shortest path from node to target using bfs
def bfs(node, target, adjlist):
    length = 0
    # we will initilaize a variabel to keep a track of visited paths
    visit = set()
    # we will add it to the visited paths
    visit.add(node)
    # we will add the nodes to be explored in a queue
    queue = deque()
    queue.append(node)

    # we will run the loop till the queue has nodes
    while queue:
        for i in range(len(queue)):
            # now we retrieve the first node from queue
            curr = queue.popleft()
            # now we will check if it is a target node or not
            if curr == target:
                return length
            
            # now lets iterate through all the neighbors in adjacency list
            for neighbor in adjlist[curr]:
                # now we check if it is already visited or not
                if neighbor not in visit:
                    # if not we add it to visited and append it to queue
                    visit.add(neighbor)
                    queue.append(neighbor)
            # since we added the length will increase
            length += 1
        return length
