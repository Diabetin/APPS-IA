from collections import deque

# Definición del grafo
graph = {
    'Inicio': ['Investigación de Mercado', 'Seleccionar País'],
    'Investigación de Mercado': [],
    'Seleccionar País': ['Establecer Oficina'],
    'Establecer Oficina': ['Llamar a Proveedores', 'Lanzamiento'],
    'Llamar a Proveedores': [],
    'Lanzamiento': []
}

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

# Ejecución del BFS
start = 'Inicio'
end = 'Lanzamiento'
path = bfs(graph, start, end)
print(path)