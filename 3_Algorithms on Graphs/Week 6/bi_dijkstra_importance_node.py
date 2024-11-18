import heapq
from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = set()
        self.shortcuts = set()
        self.contracted_neighbors = 0
        self.shortcut_cover = 0
        self.level = 0
        self.importance = 0

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, node1, node2, distance):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[node1].neighbors.add(node2)
        self.nodes[node2].neighbors.add(node1)
        self.edges[(node1, node2)] = distance
        self.edges[(node2, node1)] = distance

    def remove_node(self, node):
        if node in self.nodes:
            for neighbor in self.nodes[node].neighbors:
                self.nodes[neighbor].neighbors.remove(node)
            del self.nodes[node]

    def add_shortcut(self, node1, node2, distance):
        self.nodes[node1].shortcuts.add(node2)
        self.nodes[node2].shortcuts.add(node1)
        self.edges[(node1, node2)] = distance
        self.edges[(node2, node1)] = distance

def euclidean_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def compute_importance(node, graph):
    ed = len(node.shortcuts) - len(node.neighbors)
    importance = ed + node.contracted_neighbors + node.shortcut_cover + node.level
    return importance

def update_node_importance(node, graph):
    node.importance = compute_importance(node, graph)

def witness_path(graph, u, v, excluded_node):
    # Initialize distances with infinity, except for the start node
    dist = defaultdict(lambda: float('inf'))
    dist[u] = 0
    # Priority queue to store nodes to visit, starting with the start node
    pq = [(0, u)]

    while pq:
        d, node = heapq.heappop(pq)
        # If we've reached the target node, check if the path is shorter than the direct edge
        if node == v:
            return d <= graph.edges.get((u, v), float('inf'))
        # Skip if we've already found a shorter path to this node
        if d > dist[node]:
            continue
        # Explore neighbors and shortcuts, excluding the node we're trying to contract
        for neighbor in graph.nodes[node].neighbors | graph.nodes[node].shortcuts:
            if neighbor != excluded_node:
                new_dist = d + graph.edges[(node, neighbor)]
                # If we've found a shorter path to the neighbor, update and add to queue
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    # If we've explored all reachable nodes and haven't found the target, return False
    return False

def contract_node(graph, node, start, goal):
    """
    Contract a node in the graph, adding shortcuts between its neighbors if necessary.
    This is a key step in graph preprocessing for faster pathfinding algorithms.
    """
    # Check if the node exists in the graph
    if node not in graph.nodes:
        return False
    print(f"Contracting node: {node}")

    # Verify that contracting this node will not disconnect the graph
    # This is crucial to maintain the graph's integrity and ensure all paths are preserved
    if not check_connectivity(graph, start, goal):
        print(f"Cannot contract node {node} as it would disconnect the graph.")
        return False
    
    # Iterate through all pairs of neighbors of the node being contracted
    # This is where we decide if shortcuts need to be added
    for u in graph.nodes[node].neighbors:
        for v in graph.nodes[node].neighbors:
            if u != v:
                # Check if there's no alternative path between u and v without going through the contracted node
                # If no such path exists, we need to add a shortcut
                if not witness_path(graph, u, v, node):
                    # Calculate the distance of the new shortcut
                    distance = graph.edges[(u, node)] + graph.edges[(node, v)]
                    # Add the shortcut to the graph
                    graph.add_shortcut(u, v, distance)
                    # Increment the shortcut cover count for both endpoints
                    # This helps in determining the importance of these nodes in future contractions
                    graph.nodes[u].shortcut_cover += 1
                    graph.nodes[v].shortcut_cover += 1

    # Update properties of neighboring nodes
    # This is necessary to maintain accurate information about the graph structure
    for neighbor in graph.nodes[node].neighbors:
        # Increment the count of contracted neighbors
        # This helps in determining the importance of this node in future contractions
        graph.nodes[neighbor].contracted_neighbors += 1
        # Update the level of the neighbor
        # The level represents how many contractions have occurred "below" this node
        graph.nodes[neighbor].level = max(graph.nodes[neighbor].level, graph.nodes[node].level + 1)
        # Recalculate the importance of the neighbor
        # The importance determines the order in which nodes are contracted
        update_node_importance(graph.nodes[neighbor], graph)

    # Remove the contracted node from the graph
    # This is the final step of the contraction process
    graph.remove_node(node)
    print(f"Node {node} contracted.")
    return True

def check_connectivity(graph, start, goal):
    # Check if there's a path from start to goal in the current graph
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph.nodes[node].neighbors)
    return False

def preprocess_graph(graph, avoid_nodes, start, goal, max_contractions=3):
    """
    Preprocesses the graph by contracting nodes to create shortcuts.

    This function aims to simplify the graph structure while preserving shortest paths.
    It does this by iteratively selecting and contracting the least important nodes,
    adding shortcuts where necessary. This process can significantly speed up
    subsequent shortest path queries.

    Key steps:
    1. Initialize a priority queue of nodes based on their importance.
    2. Iteratively select and attempt to contract the least important nodes.
    3. If a node can be contracted, update the graph and node importances.
    4. Continue until reaching the maximum number of contractions or processing all nodes.

    Args:
        graph (Graph): The graph to preprocess.
        avoid_nodes (list): Nodes that should not be contracted (e.g., start and goal nodes).
        start (int): The start node of the planned route.
        goal (int): The goal node of the planned route.
        max_contractions (int): Maximum number of nodes to contract.

    Returns:
        None: The function modifies the graph in-place.
    """
    # Initialize a priority queue with nodes sorted by their importance
    # Exclude nodes that are in the avoid_nodes list
    pq = [(compute_importance(node, graph), node.value) for node in graph.nodes.values() if node.value not in avoid_nodes]
    heapq.heapify(pq)

    # Initialize counters and sets
    contractions = 0  # Keep track of how many nodes have been contracted
    non_contractible_nodes = set()  # Set to store nodes that can't be contracted

    # Continue contracting nodes until the queue is empty or we reach max_contractions
    while pq and contractions < max_contractions:
        # Get the node with the lowest importance (highest priority) from the queue
        _, node_value = heapq.heappop(pq)

        # Skip this node if it's no longer in the graph, should be avoided, or is non-contractible
        if node_value not in graph.nodes or node_value in avoid_nodes or node_value in non_contractible_nodes:
            continue

        # Attempt to contract the node
        if not contract_node(graph, node_value, start, goal):
            non_contractible_nodes.add(node_value)  # Mark node as non-contractible if contraction fails
            continue  # Move to the next node

        contractions += 1  # Increment the count of successfully contracted nodes

        # Rebuild the priority queue after each successful contraction
        # This ensures that node importances are up-to-date after the graph structure has changed
        pq = [(compute_importance(node, graph), node.value) for node in graph.nodes.values() 
              if node.value not in avoid_nodes and node.value not in non_contractible_nodes]
        heapq.heapify(pq)

def bidirectional_dijkstra(graph, start, goal):
    """
    Implements the bidirectional Dijkstra's algorithm to find the shortest path between start and goal nodes.
    
    This function works by simultaneously running two Dijkstra searches:
    1. A forward search from the start node
    2. A backward search from the goal node
    
    The algorithm terminates when the two searches meet, which often happens before either search has explored the entire graph.
    This can lead to significant performance improvements over the standard Dijkstra's algorithm.
    
    The function uses both regular edges and shortcuts (if any) added during the graph preprocessing stage.
    
    Logical flow:
    1. Initialize data structures for both forward and backward searches
    2. Alternately expand the forward and backward searches
    3. For each node processed, update distances and check if we've met the other search direction
    4. If searches meet, reconstruct the path and calculate total distance
    5. Return the path and distance, or None and infinity if no path exists
    
    Args:
    graph (Graph): The graph to search
    start: The starting node
    goal: The goal node
    
    Returns:
    tuple: (path, distance) where path is a list of nodes and distance is the total path length,
           or (None, inf) if no path exists
    """
    # If start and goal are the same, return immediately
    if start == goal:
        return [start], 0

    # Initialize data structures for both forward and backward searches
    # dist: dictionary to store distances from start/goal
    # parent: dictionary to store parent nodes for path reconstruction
    # pq: priority queue for selecting next node to process
    # visited: set of nodes that have been fully processed
    forward_dist = {start: 0}
    backward_dist = {goal: 0}
    forward_parent = {}
    backward_parent = {}
    forward_pq = [(0, start)]
    backward_pq = [(0, goal)]
    forward_visited = set()
    backward_visited = set()

    def process_node(dist, parent, pq, visited, current, direction):
        """
        Helper function to process a node in either the forward or backward direction.
        
        This function is crucial for the bidirectional Dijkstra algorithm. It performs the following tasks:
        1. Marks the current node as visited
        2. Explores all neighbors and shortcuts of the current node
        3. Updates distances and parents for neighbors if a shorter path is found
        4. Adds updated neighbors to the priority queue for future processing
        5. Checks if the current node has been visited by the opposite search direction
        
        Args:
        dist (dict): Distance dictionary for the current direction
        parent (dict): Parent dictionary for the current direction
        pq (list): Priority queue for the current direction
        visited (set): Set of visited nodes for the current direction
        current: The current node being processed
        direction (str): Either "forward" or "backward", indicating the search direction
        
        Returns:
        The meeting node if the searches have met, None otherwise
        """
        # Mark current node as visited
        visited.add(current)
        
        # Explore both regular neighbors and shortcut connections
        for neighbor in graph.nodes[current].neighbors | graph.nodes[current].shortcuts:
            new_dist = dist[current] + graph.edges[(current, neighbor)]
            
            # Update distance if we've found a shorter path
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

        # Check if we've met the other search direction
        # This is the key to bidirectional search - we stop when the two searches meet
        if current in (forward_visited if direction == "backward" else backward_visited):
            return current
        return None

    meeting_node = None
    # Main loop of bidirectional search
    # We alternate between forward and backward search until they meet
    while forward_pq and backward_pq:
        # Forward search step
        _, current_forward = heapq.heappop(forward_pq)
        meeting_node = process_node(forward_dist, forward_parent, forward_pq, forward_visited, current_forward, "forward")
        if meeting_node:
            break

        # Backward search step
        _, current_backward = heapq.heappop(backward_pq)
        meeting_node = process_node(backward_dist, backward_parent, backward_pq, backward_visited, current_backward, "backward")
        if meeting_node:
            break

    # If no meeting point found, there's no path between start and goal
    if meeting_node is None:
        return None, float('inf')

    # Reconstruct the full path
    path = []
    # First, build the path from start to meeting node
    current = meeting_node
    while current != start:
        path.append(current)
        current = forward_parent[current]
    path.append(start)
    path = path[::-1]  # Reverse to get correct order

    # Then, build the path from meeting node to goal
    current = meeting_node
    while current != goal:
        current = backward_parent[current]
        path.append(current)

    # Calculate total distance by summing distances from both directions
    total_distance = forward_dist[meeting_node] + backward_dist[meeting_node]
    return path, total_distance

def main():
    graph = Graph()

    n, m = map(int, input().split())

    print("Enter point coordinates (x, y)")

    nodes = []
    for _ in range(n):
        x, y = map(int, input().split())
        coord = (x, y)
        nodes.append(coord)
        graph.add_node(coord)

    print("Enter edges")
    for _ in range(m):
        u, v = map(int, input().split())
        distance = euclidean_distance(nodes[u], nodes[v])
        graph.add_edge(nodes[u], nodes[v], distance)
    
    print("Preprocessing graph...")
    # Avoid contracting the start and goal nodes
    start_x, start_y = map(int, input("Enter start coordinates (x, y): ").split())
    goal_x, goal_y = map(int, input("Enter goal coordinates (x, y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    avoid_nodes = {start, goal}
    
    # Preprocess the graph with a check for connectivity before contracting nodes
    preprocess_graph(graph, avoid_nodes, start, goal, max_contractions=3)
    print("Preprocessing complete.")

    print("Nodes in graph:", list(graph.nodes.keys()))
    print("Edges in graph:", list(graph.edges.keys()))

    path, distance = bidirectional_dijkstra(graph, start, goal)

    if path:
        print(f"Shortest path: {path}")
        print(f"Distance: {distance}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()

"""


8 10
Enter point coordinates (x, y)
0 0
1 1
2 0
2 2
3 1
4 2
5 0
5 2
Enter edges
0 1
0 2
1 2
1 3
2 3
3 4
3 5
4 5
4 6
5 7
Selected 4 landmarks on the border
Enter start coordinates (x, y): 0 0
Enter goal coordinates (x, y)5 0


Output:

Preprocessing graph...
Enter start coordinates (x, y): 0 0
Enter goal coordinates (x, y): 5 0
Contracting node: (2, 2)
Node (2, 2) contracted.
Contracting node: (5, 2)
Cannot contract node (5, 2) as it would disconnect the graph.
Contracting node: (2, 0)
Cannot contract node (2, 0) as it would disconnect the graph.
Contracting node: (4, 2)
Cannot contract node (4, 2) as it would disconnect the graph.
Contracting node: (1, 1)
Cannot contract node (1, 1) as it would disconnect the graph.
Contracting node: (3, 1)
Cannot contract node (3, 1) as it would disconnect the graph.
Preprocessing complete.
Nodes in graph: [(0, 0), (1, 1), (2, 0), (3, 1), (4, 2), (5, 0), (5, 2)]
Edges in graph: [((0, 0), (1, 1)), ((1, 1), (0, 0)), ((0, 0), (2, 0)), ((2, 0), (0, 0)), ((1, 1), (2, 0)), ((2, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (1, 1)), ((2, 0), (2, 2)), ((2, 2), (2, 0)), ((2, 2), (3, 1)), ((3, 1), (2, 2)), ((2, 2), (4, 2)), ((4, 2), (2, 2)), ((3, 1), (4, 2)), ((4, 2), (3, 1)), ((3, 1), (5, 0)), ((5, 0), (3, 1)), ((4, 2), (5, 2)), ((5, 2), (4, 2)), ((3, 1), (1, 1)), ((1, 1), (3, 1))]
Shortest path: [(0, 0), (1, 1), (3, 1), (5, 0)]
Distance: 6.4787086646190755

"""