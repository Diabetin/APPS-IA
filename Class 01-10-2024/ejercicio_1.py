from collections import deque

# Grafo con las especificaciones proporcionadas
graph = {
    'Inicio': {'Planificación': 'AND', 'Diseño': 'AND'},
    'Planificación': {'Publicidad': 'OR'},
    'Diseño': {'Fabricación': 'OR'},
    'Publicidad': {'Fabricación': 'AND'},
    'Fabricación': {'Evento': 'AND'}
}

# BFS en un grafo AND-OR
def bfs_and_or(graph, start, end):
    # Cola para BFS
    queue = deque([[start]])
    # Conjunto para registrar nodos visitados
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        # Si alcanzamos el nodo final
        if node == end:
            return path

        # Marcar el nodo como visitado
        visited.add(node)

        # Explorar los vecinos en el orden adecuado
        for neighbor, condition in graph.get(node, {}).items():
            # Si es un nodo AND, avanzar solo si todos los nodos necesarios están visitados
            if condition == 'OR':
                if all(predecessor in visited for predecessor in graph if neighbor in graph.get(predecessor, {})):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
            # Si es un nodo OR, agregar el camino directamente
            elif condition == 'AND':
                if neighbor not in visited:  # Evitar volver a visitar nodos
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None

# Ejecución del BFS
start_node = 'Inicio'
end_node = 'Evento'
path = bfs_and_or(graph, start_node, end_node)
print(path)
