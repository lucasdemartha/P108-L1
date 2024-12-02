import heapq

# Mapeamento das cidades e suas conexões (arestas)
grafo = {
    'Santa Rita do Sapucaí': {'Paraisópolis': 70, 'Cristina': 50, 'Estiva': 30, 'Pedralva': 35},
    'Pouso Alegre': {'Camanducaia': 64, 'Wenceslau Braz': 70, 'Gonçalves': 50, 'Brazópolis': 60},
    'Itajubá': {'Piranguinho': 17, 'Cachoeira de Minas': 64, 'Brazópolis': 36, 'Conceição dos Ouros': 30, 'Cambuí': 92},
    # Adicionar as demais cidades e distâncias
}

# Função de Dijkstra
def dijkstra(grafo, inicio):
    distancias = {cidade: float('infinity') for cidade in grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]
    
    while pq:
        dist_atual, cidade_atual = heapq.heappop(pq)
        
        if dist_atual > distancias[cidade_atual]:
            continue
        
        for vizinho, peso in grafo[cidade_atual].items():
            distancia = dist_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(pq, (distancia, vizinho))
    
    return distancias

# Executando o algoritmo a partir de 'Santa Rita do Sapucaí'
resultado = dijkstra(grafo, 'Santa Rita do Sapucaí')
print(resultado)
