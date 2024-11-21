def crear_grafo():
    grafo = {
        'A': {'B': 2, 'C': 5},
        'B': {'C': 8, 'D': 7},
        'C': {'E': 4, 'D': 2},
        'D': {'F': 1},
        'E': {'F': 3, 'D': 6},
        'F': {'F': 0}
    }
    return grafo

grafo = crear_grafo()

print("El grafo dirigido con pesos no negativos es: \n {} \n".format(grafo))

nodo_inicio = input("Introduce el nodo de inicio de la siguiente lista \n {} - ".format(grafo.keys()))
while nodo_inicio not in grafo.keys():
    nodo_inicio = input("Introduce el nodo de inicio de la siguiente lista \n {} - ".format(grafo.keys()))

nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))
while nodo_final not in grafo.keys():
    nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))

while nodo_inicio == nodo_final:
    print("El nodo de inicio y el nodo final son el mismo.")
    nodo_final = input("Introduce el nodo final de la siguiente lista \n {} - ".format(grafo.keys()))
    
nodo_origen = nodo_inicio
ruta = {}
cola = []

for nodo in grafo:
    ruta[nodo] = float('inf')
    cola.append(nodo)

print("Diccionario inicial de rutas: \n {}".format(ruta))
print("Lista inicial de nodos en cola: \n {}".format(cola))

distancia = []
visitados = []

while nodo_inicio != nodo_final:
    try:
        ruta[nodo_inicio] = 0
        nodos_conectados = grafo[nodo_inicio]

        menor_distancia = min(nodos_conectados.values())
        siguiente_nodo = None

        for vecino in grafo[nodo_inicio]:
            if grafo[nodo_inicio][vecino] == menor_distancia and vecino not in visitados:
                distancia.append(menor_distancia)
                visitados.append(vecino)
                siguiente_nodo = vecino

        nodo_inicio = siguiente_nodo
        
        if nodo_inicio == nodo_final:
            print("Has llegado a tu destino.")
            ruta_final = ' -> '.join([str(nodo) for nodo in visitados])
            print("Ruta seguida: {} -> {}".format(nodo_origen, ruta_final))
            print("Costo total: {}".format(sum(distancia)))
    
    except KeyError:
        print("No es posible llegar al nodo final desde este nodo de inicio, no hay camino disponible.")
        break

