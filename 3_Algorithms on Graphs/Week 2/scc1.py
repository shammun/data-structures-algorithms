def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[vertex]:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)
    
def get_sink_components(graph):
    # Step 1: Create the reversed graph GR
    reversed_graph = {v: [] for v in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            reversed_graph[neighbor].append(vertex)
            
    # Step 2: Run DFS on GR to determine finishing time
    visited = {v: False for v in reversed_graph}
    stack = []
    for vertex in reversed_graph:
        if not visited[vertex]:
            dfs(reversed_graph, vertex, visited, stack)
    
    # Step 3: Sort vertices in reversed order based on finishing time
    sorted_vertices = stack[::-1]
    
    # Step 4: Identify the sink components
    visited = {v: False for v in graph}
    sink_components = []
    for vertex in sorted_vertices:
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            sink_components.append(component)
    return sink_components
    
graph = {
    'A': ['B'],
    'B': ['C', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['E'],
    'E': ['F'],
    'F': ['G'],
    'G': ['F', 'H'],
    'H': ['I'],
    'I': ['J'],
    'J': ['H']
}
sink_components = get_sink_components(graph)
print("Sink Components of G:")
for component in sink_components:
    print(component)