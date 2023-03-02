#Tâche: Écrivez une fonction en Python qui implémente un algorithme de tri topologique sur un graphe orienté acyclique représenté sous la forme d'un dictionnaire où les clés sont les nœuds et les valeurs sont des listes de nœuds adjacents. 

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in in_degree if in_degree[node] == 0]

    sorted_nodes = []

    while queue:
        current = queue.pop(0)
        sorted_nodes.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_nodes) != len(graph):
        raise ValueError("Le graphe contient un cycle.")

    return sorted_nodes

graph = {
    5: [11],
    11: [11, 8],
    3: [8, 10],
    11: [2, 9, 10],
    8: [9],
}
sorted_nodes = topological_sort(graph)
print(sorted_nodes)