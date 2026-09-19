# Mapa_metro

Modelo simplificado del Metro CDMX como un grafo no dirigido.

## Uso rápido

```python
from metro_graph import build_default_cdmx_metro_map

metro = build_default_cdmx_metro_map()
print(metro.bfs_route("Observatorio", "Pantitlan"))
print(metro.dfs_route("Observatorio", "Pantitlan"))
```

- `bfs_route(inicio, fin)` calcula una ruta mínima en número de estaciones.
- `dfs_route(inicio, fin)` calcula una ruta válida usando recorrido en profundidad.
