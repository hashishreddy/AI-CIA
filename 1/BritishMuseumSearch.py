

def british_museum_search(graph, start, goal):
    all_paths = []

    def dfs(node, visited, path):
        if node == goal:
            all_paths.append(path + [node])
            return
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                dfs(neighbor, visited + [neighbor], path + [node])

    dfs(start, [], [])

    best_path = None
    min_cost = float('inf')

    for path in all_paths:
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        if cost < min_cost:
            min_cost = cost
            best_path = path

    print(f"Best Path: {best_path} \n cost {min_cost}")
    return best_path

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 1, 'G': 2},
    'E': {'B': 5, 'G': 3},
    'F': {'C': 4, 'G': 6},
    'G': {'D': 2, 'E': 3, 'F': 6}
}

british_museum_search(graph, 'S', 'G')
