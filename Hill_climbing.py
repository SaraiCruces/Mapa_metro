class TareaBusqueda:
    def __init__(self, punto_inicio, objetivo):
        self.punto_inicio = punto_inicio 
        self.objetivo = objetivo 
    
    def obtener_movimientos(self, estado):
        raise NotImplementedError

    def estado_siguiente(self, estado, movimiento):
        raise NotImplementedError

    def meta_alcanzada(self, estado):
        return self.objetivo == estado
    
    def calcular_costo(self, estado_a, movimiento, estado_b):
        return 1
   
    def valor_heuristico(self, estado):
        return 0

class ProblemaRutaMapa(TareaBusqueda):
    def __init__(self, punto_inicio, objetivo, mapa_grafo):
        super().__init__(punto_inicio, objetivo)
        self.mapa_grafo = mapa_grafo
    
    def obtener_movimientos(self, estado):
        opciones = []
        for destino in self.mapa_grafo[estado].keys():
            opciones.append(destino)
        return opciones

    def estado_siguiente(self, estado, movimiento):
        return movimiento

    def calcular_costo(self, estado_a, movimiento, estado_b):
        return self.mapa_grafo[estado_a][estado_b]
   
    def valor_heuristico(self, estado):
        return distancia_estimada[estado]

class EstadoRuta:
    def __init__(self, estado, nodo_origen=None, accion_tomada=None, costo_acumulado=0):
        self.estado = estado
        self.nodo_origen = nodo_origen
        self.accion_tomada = accion_tomada
        self.costo_acumulado = costo_acumulado

    def obtener_trayectoria(self):
        camino_recorrido = []
        nodo_temp = self
        while nodo_temp:
            camino_recorrido.append(nodo_temp.estado)
            nodo_temp = nodo_temp.nodo_origen
        return camino_recorrido[::-1]

    def generar_sucesores(self, problema):
        sucesores = []
        for accion in problema.obtener_movimientos(self.estado):
            sucesores.append(self.crear_hijo(problema, accion))
        return sucesores

    def crear_hijo(self, problema, accion):
        siguiente = problema.estado_siguiente(self.estado, accion)
        costo_paso = problema.calcular_costo(self.estado, accion, siguiente)
        return EstadoRuta(siguiente, self, accion, self.costo_acumulado + costo_paso)

mapa_ciudades = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucarest': 101},
    'Bucarest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucarest': 90},
    'Urziceni': {'Bucarest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
}

distancia_estimada = {
    'Arad': 366, 'Bucarest': 0, 'Craiova': 160, 'Dobreta': 242,
    'Eforie': 161, 'Fagaras': 178, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 98, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374,
}

def busqueda_ascenso_colina(problema):
    nodo_actual = EstadoRuta(problema.punto_inicio)

    while True:
        if problema.meta_alcanzada(nodo_actual.estado):
            return nodo_actual
        adyacentes = nodo_actual.generar_sucesores(problema)
        if not adyacentes:
            return nodo_actual
        opcion_ideal = min(adyacentes, key=lambda n: problema.valor_heuristico(n.estado))
        if problema.valor_heuristico(opcion_ideal.estado) >= problema.valor_heuristico(nodo_actual.estado):
            return nodo_actual
        nodo_actual = opcion_ideal

if __name__ == "__main__":
    instancia_problema = ProblemaRutaMapa("Arad", "Bucarest", mapa_ciudades)
    resultado_final = busqueda_ascenso_colina(instancia_problema)

    print("--- Resultados de Búsqueda ---")
    print(f"Ruta tomada: {' -> '.join(resultado_final.obtener_trayectoria())}")
    print(f"Costo acumulado (distancia de viaje): {resultado_final.costo_acumulado} km")