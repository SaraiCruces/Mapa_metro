from collections import deque


class MetroCDMXGraph:
    """Representa una parte del mapa del Metro CDMX como un grafo no dirigido."""

    def __init__(self):
        self._graph = {}

    def add_station(self, station):
        self._graph.setdefault(station, set())

    def add_connection(self, station_a, station_b):
        self.add_station(station_a)
        self.add_station(station_b)
        self._graph[station_a].add(station_b)
        self._graph[station_b].add(station_a)

    def bfs_route(self, start, end):
        if start not in self._graph or end not in self._graph:
            return None
        if start == end:
            return [start]

        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            station, path = queue.popleft()
            for neighbor in sorted(self._graph[station]):
                if neighbor in visited:
                    continue
                next_path = path + [neighbor]
                if neighbor == end:
                    return next_path
                visited.add(neighbor)
                queue.append((neighbor, next_path))

        return None

    def dfs_route(self, start, end):
        if start not in self._graph or end not in self._graph:
            return None
        if start == end:
            return [start]

        stack = [(start, [start])]
        visited = set()

        while stack:
            station, path = stack.pop()
            if station in visited:
                continue
            visited.add(station)

            for neighbor in sorted(self._graph[station], reverse=True):
                if neighbor in visited:
                    continue
                next_path = path + [neighbor]
                if neighbor == end:
                    return next_path
                stack.append((neighbor, next_path))

        return None


def build_default_cdmx_metro_map():
    """Construye una red simplificada del Metro CDMX para calcular rutas."""
    metro = MetroCDMXGraph()

    connections = [
        ("Observatorio", "Tacubaya"),
        ("Tacubaya", "Balderas"),
        ("Balderas", "Pino Suarez"),
        ("Pino Suarez", "Pantitlan"),
        ("Tacubaya", "Centro Medico"),
        ("Centro Medico", "Chabacano"),
        ("Chabacano", "Pantitlan"),
        ("Balderas", "Hidalgo"),
        ("Hidalgo", "Bellas Artes"),
        ("Bellas Artes", "Pino Suarez"),
    ]

    for station_a, station_b in connections:
        metro.add_connection(station_a, station_b)

    return metro
