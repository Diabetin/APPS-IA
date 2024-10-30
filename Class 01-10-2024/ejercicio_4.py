from collections import deque

# Representación del grafo
graph = {
    'Conceptualizacion':{'Investigacion de Mercado':'OR','Diseño de Prototipo':'OR'},
    'Diseño de Prototipo':{'Evaluacion'},
    'Evaluacion':{'Lanzamiento'}
}
from collections import deque

def bfs(graph, start, goal):
    # Cola para realizar la búsqueda y lista de nodos visitados
    queue = deque([[start]])
    visited = set()

    # Bucle principal del BFS
    while queue:
        # Obtener el primer camino de la cola
        path = queue.popleft()
        node = path[-1]

        # Si llegamos al objetivo, retornamos el camino
        if node == goal:
            return path

        # Si el nodo no ha sido visitado
        elif node not in visited:
            # Marcar el nodo como visitado
            visited.add(node)

            # Obtener nodos adyacentes y agregar caminos nuevos a la cola
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    # Retornar None si no se encontró un camino
    return None

# Ejecución del algoritmo
start_node = "Conceptualizacion"
goal_node = "Lanzamiento"
optimal_path = bfs(graph, start_node, goal_node)

print(optimal_path)

