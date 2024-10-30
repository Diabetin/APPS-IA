from collections import deque

def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path


        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 


    return None


# Definición del grafo
graph = {
    'Inicio': ['Rediseño', 'Investigación de Nuevas Funciones'],
    'Rediseño': ['Testear Prototipo'],
    'Investigación de Nuevas Funciones': ['Testear Prototipo'],
    'Testear Prototipo': ['Evaluar'],
    'Evaluar': ['Lanzar'],
    'Lanzar': []
}

# Ejecución de DFS
start = 'Inicio'
end = 'Lanzar'
path = bfs(graph, start, end)
print(path)
