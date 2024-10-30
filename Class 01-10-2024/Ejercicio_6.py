from collections import deque
# Grafo organizados segun las especificaciones solicitadas
graph = {
    "Inicio": ["Diseñar UI", "Desarrollo Backend"],
    "Diseñar UI": [],
    "Desarrollo Backend": ["Testear"],
    "Testear": ["Desplegar"],
    "Desplegar": ["Aplicación Completa"],
    "Aplicación Completa": []
}

def dfs(graph, node, visited):
    # Evitar ciclos
    if node in visited:
        return []
    visited.add(node)

    # Inicia la secuencia con el nodo actual
    path = [node]

    # Recorrer cada conexión del nodo actual
    for neighbor in graph[node]:
        path.extend(dfs(graph, neighbor, visited))
    
    return path

# Función para encontrar el camino completo desde "Inicio" hasta "Aplicación Completa"
def find_path(graph):
    visited = set()
    return dfs(graph, "Inicio", visited)

# Ejecutar el algoritmo DFS para encontrar el camino
path = find_path(graph)
print("Camino encontrado:", path)
