import heapq

def crear_grafo():
    grafo = {
        'A': {'B': 2, 'C': 5},
        'B': {'C': 8, 'D': 7},
        'C': {'E': 4, 'D': 2},
        'D': {'F': 1},
        'E': {'F': 3, 'D': 6},
        'F': {}
    }
    return grafo

def dijkstra(grafo, inicio, final):
    # Cola de prioridad para manejar los nodos por distancia mínima
    cola_prioridad = []
    # Distancias mínimas desde el nodo inicial a todos los demás nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    # Predecesores para reconstruir la ruta
    predecesores = {nodo: None for nodo in grafo}
    # Insertar el nodo inicial en la cola de prioridad
    heapq.heappush(cola_prioridad, (0, inicio))
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si hemos llegado al nodo final, terminamos
        if nodo_actual == final:
            break

        # Procesar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                # Actualizar la distancia si encontramos un camino más corto
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    # Reconstruir la ruta desde el nodo final al inicial
    ruta = []
    nodo = final
    while nodo:
        ruta.append(nodo)
        nodo = predecesores[nodo]
    ruta.reverse()  # La ruta está al revés, la invertimos
    
    return distancias[final], ruta if distancias[final] != float('inf') else None

# Ejecución del programa
if __name__ == "__main__":
    grafo = crear_grafo()
    print("El grafo dirigido con pesos no negativos es: \n", grafo, "\n")

    nodo_inicio = input("Introduce el nodo de inicio de la siguiente lista \n {} - ".format(grafo.keys()))
    while nodo_inicio not in grafo.keys():
        nodo_inicio = input("Introduce el nodo de inicio de la siguiente lista \n {} - ".format(grafo.keys()))

    nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))
    while nodo_final not in grafo.keys():
        nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))

    while nodo_inicio == nodo_final:
        print("El nodo de inicio y el nodo final son el mismo.")
        nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))
    
    # Ejecutar el algoritmo de Dijkstra
    costo_total, ruta = dijkstra(grafo, nodo_inicio, nodo_final)
    
    if ruta:
        print("\nLa ruta más corta desde '{}' hasta '{}' es:".format(nodo_inicio, nodo_final))
        print(" -> ".join(ruta))
        print("Costo total: {}".format(costo_total))
    else:
        print("\nNo hay un camino desde '{}' hasta '{}'.".format(nodo_inicio, nodo_final))
