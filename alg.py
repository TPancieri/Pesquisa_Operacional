NETWORK = {
    'A': {'B': 40, 'C': 30},
    'B': {'A': 40, 'C': 50, 'D': 20},
    'C': {'A': 30, 'B': 50, 'D': 10, 'E': 30},
    'D': {'B': 20, 'C': 10, 'E': 40, 'F': 20},
    'E': {'C': 30, 'D': 40, 'F': 30},
    'F': {'D': 20, 'E': 30}
}

def initialize_distances(network, start):
    """
    Inicializa as distâncias para todos os nós como infinito, menos para o nó inicial.
    
    Args:
        network: dicionário representando a network
        start: nó inicial
    Returns:
        dict: dicionário com as distâncias iniciais
    """
    distances = {router: float('infinity') for router in network}
    distances[start] = 0
    return distances

def initialize_previous_nodes(network):
    """
    Inicializa o dicionário que guarda o caminho anterior de cada nó.
    
    Args:
        network: dicionário representando a network
        
    Returns:
        dict: dicionário com os nós anteriores
    """
    return {router: None for router in network}

def find_closest_unvisited_node(distances, unvisited):
    """
    Encontra o nó não visitado com a menor distância.
    
    Args:
        distances: dicionário com as distâncias atuais
        unvisited: lista de nós não visitados
        
    Returns:
        str: nó mais próximo não visitado
    """
    return min(unvisited, key=lambda x: distances[x])

def update_distances(current, distances, previous, unvisited, network):
    """
    Atualiza as distâncias para os vizinhos do nó atual.
    
    Args:
        current: nó atual sendo processado
        distances: dicionário com as distâncias atuais
        previous: dicionário com os nós anteriores
        unvisited: lista de nós não visitados
        network: dicionário representando a rede
    """
    for neighbor, latency in network[current].items():
        if neighbor not in unvisited:
            continue
            
        distance_through_current = distances[current] + latency
        
        if distance_through_current < distances[neighbor]:
            distances[neighbor] = distance_through_current
            previous[neighbor] = current

def construct_path(previous, end):
    """
    Constrói o caminho do fim para o início.
    
    Args:
        previous: dicionário com os nós anteriores
        end: nó final
        
    Returns:
        list: caminho do início ao fim
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]

def find_shortest_path(start, end):
    """
    Encontra o caminho mais curto entre dois nós em uma network.
    
    Args:
        start: nó inicial
        end: nó final
        
    Returns:
        tuple: (caminho, latência_total)
    """

    distances = initialize_distances(NETWORK, start)
    previous = initialize_previous_nodes(NETWORK)
    unvisited = list(NETWORK.keys())
    
    while unvisited:
        current = find_closest_unvisited_node(distances, unvisited)
        
        if current == end:
            break
            
        unvisited.remove(current)
        update_distances(current, distances, previous, unvisited, NETWORK)
    

    path = construct_path(previous, end)
    return path, distances[end] 
