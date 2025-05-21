NETWORK = {
    'A': {'B': 40, 'C': 30},
    'B': {'A': 40, 'C': 50, 'D': 20},
    'C': {'A': 30, 'B': 50, 'D': 10, 'E': 30},
    'D': {'B': 20, 'C': 10, 'E': 40, 'F': 20},
    'E': {'C': 30, 'D': 40, 'F': 30},
    'F': {'D': 20, 'E': 30}
}

def find_shortest_path(start, end):
    """
    Encontra o caminho mais curto entre dois roteadores em uma rede.
    
    start: nó inicial
    end: nó final
        
    Retorna: (caminho, latência_total)
    """
    # Inicializa as distâncias para todos os nós como infinito 
    distances = {}
    for router in NETWORK:
        distances[router] = float('infinity')
    # Distância do ponto de partida é zero
    distances[start] = 0

    # Inicializa o dicionário que vai guardar o caminho
    # Para cada nó, armazena qual foi o nó anterior no caminho mais curto
    previous = {}
    for router in NETWORK:
        previous[router] = None
    
    # Lista de nós que ainda não foram visitados
    unvisited = list(NETWORK.keys())
    
    while unvisited:
        # Encontra o nó não visitado com a menor distância
        current = min(unvisited, key=lambda x: distances[x])
        
        if current == end:
            break
            
        # Remove da lista de não visitado
        unvisited.remove(current)
        
        # Obtém todos os vizinhos do nó atual
        neighbors = NETWORK[current]
        
        # Para cada vizinho verifica se tem um caminho mais curto
        for neighbor, latency in neighbors.items():
            # Só analisa vizinhos que ainda não foram visitados
            if neighbor not in unvisited:
                continue
                
            # Calcula a distância total até este vizinho passando pelo nó atual
            distance_through_current = distances[current] + latency
            
            # Se encontramos um caminho mais curto até este vizinho
            if distance_through_current < distances[neighbor]:
                # Atualiza a menor distância conhecida até este vizinho
                distances[neighbor] = distance_through_current
                # Registra que o melhor caminho para este vizinho passa pelo nó atual
                previous[neighbor] = current
    
    # Constrói o caminho do fim para o início
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    # Retorna o caminho (invertido para ir do início ao fim) e latência total
    return path[::-1], distances[end] 

find_shortest_path("A", "E")
