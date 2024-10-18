

def oracle_search(graph, start, goal):
    path = ['A', 'B', 'D', 'G']  
    cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
    print(f"Best Path: {path} \n cost {cost}")
    return path

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 1, 'G': 2},
    'E': {'B': 5, 'G': 3},
    'F': {'C': 4, 'G': 6},
    'G': {'D': 2, 'E': 3, 'F': 6}
}
oracle_search(graph, 'A', 'G')
