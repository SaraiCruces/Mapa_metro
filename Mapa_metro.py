from collections import deque

class Problem:
    def __init__(self, initial, goal):
        self.initial = initial 
        self.goal = goal 
    
    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        return self.goal == state
    
    def action_cost(self, state1, action, state2):
        return 1
   
    def h(self, state):
        return 0

class GraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph
    
    def actions(self, state):
        lista = []
        for key in self.graph[state].keys():
            lista.append(key)
        return lista

    def result(self, state, action):
        return action

    def action_cost(self, state1, action, state2):
        return self.graph[state1][state2]

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def path(self):
        lista_path = []
        node = self
        while node:
            lista_path.append(node.state)
            node = node.parent
        return lista_path[::-1]

    def expand(self, problem):
        lista = []
        for action in problem.actions(self.state):
            lista.append(self.child_node(problem, action))
        return lista

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        step_cost = problem.action_cost(self.state, action, next_state)
        return Node(next_state, self, action, self.path_cost + step_cost)

def depth_first_graph_search(problem):
    start_node = Node(problem.initial)
    if problem.is_goal(start_node.state):
        return start_node
    frontier = [start_node]
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node.state)

        if problem.is_goal(node.state):
            return node

        for child in node.expand(problem):
            if child.state not in explored:
                frontier.append(child)
    return None

def breadth_first_graph_search(problem):
    start_node = Node(problem.initial)
    if problem.is_goal(start_node.state):
        return start_node
    frontier = deque([start_node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        if problem.is_goal(node.state):
            return node

        for child in node.expand(problem):
            if child.state not in explored:
                frontier.append(child)
    return None

metro = {}

# Linea 1
metro['observatorio'] = ['tacubaya']
metro['juanacatlan'] = ['tacubaya', 'chapultepec']
metro['chapultepec'] = ['juanacatlan', 'sevilla']
metro['sevilla'] = ['chapultepec', 'insurgentes']
metro['insurgentes'] = ['sevilla', 'cuauhtemoc']
metro['cuauhtemoc'] = ['insurgentes', 'balderas']
metro['balderas'] = ['cuauhtemoc', 'salto_del_agua', 'juarez', 'ninos_heroes']
metro['salto_del_agua'] = ['balderas', 'isabel_la_catolica', 'san_juan_de_letran', 'doctores']
metro['isabel_la_catolica'] = ['salto_del_agua', 'pino_suarez']
metro['pino_suarez'] = ['isabel_la_catolica', 'merced', 'zocalo', 'san_antonio_abad']
metro['merced'] = ['pino_suarez', 'candelaria']
metro['candelaria'] = ['merced', 'san_lazaro', 'morelos', 'fray_servando']
metro['san_lazaro'] = ['candelaria', 'moctezuma', 'morelos', 'flores_magon']
metro['moctezuma'] = ['san_lazaro', 'balbuena']
metro['balbuena'] = ['moctezuma', 'boulevard_puerto_aereo']
metro['boulevard_puerto_aereo'] = ['balbuena', 'gomez_farias']
metro['gomez_farias'] = ['boulevard_puerto_aereo', 'zaragoza']
metro['zaragoza'] = ['gomez_farias', 'pantitlan']

# Linea 2
metro['cuatro_caminos'] = ['panteones']
metro['panteones'] = ['cuatro_caminos', 'tacuba']
metro['cuitlahuac'] = ['tacuba', 'popotla']
metro['popotla'] = ['cuitlahuac', 'colegio_militar']
metro['colegio_militar'] = ['popotla', 'normal']
metro['normal'] = ['colegio_militar', 'san_cosme']
metro['san_cosme'] = ['normal', 'revolucion']
metro['revolucion'] = ['san_cosme', 'hidalgo']
metro['hidalgo'] = ['revolucion', 'bellas_artes', 'guerrero', 'juarez']
metro['bellas_artes'] = ['hidalgo', 'allende', 'garibaldi', 'san_juan_de_letran']
metro['san_juan_de_letran'] = ['salto_del_agua', 'bellas_artes']
metro['allende'] = ['bellas_artes', 'zocalo']
metro['zocalo'] = ['allende', 'pino_suarez']
metro['san_antonio_abad'] = ['pino_suarez', 'chabacano']
metro['viaducto'] = ['chabacano', 'xola']
metro['xola'] = ['viaducto', 'villa_de_cortes']
metro['villa_de_cortes'] = ['xola', 'nativitas']
metro['nativitas'] = ['villa_de_cortes', 'portales']
metro['portales'] = ['nativitas', 'ermita']
metro['ermita'] = ['portales', 'general_anaya', 'eje_central', 'mexicaltzingo']
metro['general_anaya'] = ['ermita', 'tasquena']
metro['tasquena'] = ['general_anaya']

# Linea 3
metro['indios_verdes'] = ['deportivo_18_de_marzo']
metro['potrero'] = ['deportivo_18_de_marzo', 'la_raza']
metro['tlatelolco'] = ['la_raza', 'guerrero']
metro['juarez'] = ['hidalgo', 'balderas']
metro['ninos_heroes'] = ['balderas', 'hospital_general']
metro['hospital_general'] = ['ninos_heroes', 'centro_medico']
metro['etiopia'] = ['centro_medico', 'eugenia']
metro['eugenia'] = ['etiopia', 'division_del_norte']
metro['division_del_norte'] = ['eugenia', 'zapata']
metro['zapata'] = ['division_del_norte', 'coyoacan']
metro['coyoacan'] = ['zapata', 'viveros']
metro['viveros'] = ['coyoacan', 'miguel_angel_de_quevedo']
metro['miguel_angel_de_quevedo'] = ['viveros', 'copilco']
metro['copilco'] = ['miguel_angel_de_quevedo', 'universidad']
metro['universidad'] = ['copilco']

# Linea 4
metro['talisman'] = ['martin_carrera', 'bondojito']
metro['bondojito'] = ['talisman', 'consulado']
metro['canal_del_norte'] = ['consulado', 'morelos']
metro['fray_servando'] = ['candelaria', 'jamaica']
metro['santa_anita'] = ['jamaica']

# Linea 5
metro['politecnico'] = ['instituto_del_petroleo']
metro['autobuses_del_norte'] = ['instituto_del_petroleo', 'la_raza']
metro['la_raza'] = ['autobuses_del_norte', 'misterios', 'potrero', 'tlatelolco']
metro['misterios'] = ['la_raza', 'valle_gomez']
metro['valle_gomez'] = ['misterios', 'consulado']
metro['consulado'] = ['valle_gomez', 'eduardo_molina', 'bondojito', 'canal_del_norte']
metro['eduardo_molina'] = ['consulado', 'aragon']
metro['aragon'] = ['eduardo_molina', 'oceania']
metro['terminal_aerea']  = ['oceania', 'hangares']
metro['hangares'] = ['terminal_aerea', 'pantitlan']

# Linea 6
metro['el_rosario'] = ['aquiles_serdan', 'tezozomoc']
metro['tezozomoc'] = ['el_rosario', 'azcapotzalco']
metro['azcapotzalco'] = ['tezozomoc', 'ferreria']
metro['ferreria'] = ['azcapotzalco', 'norte_45']
metro['norte_45'] = ['ferreria', 'vallejo']
metro['vallejo'] = ['norte_45', 'instituto_del_petroleo']
metro['instituto_del_petroleo'] = ['politecnico', 'lindavista', 'autobuses_del_norte']
metro['lindavista'] = ['instituto_del_petroleo', 'deportivo_18_de_marzo']
metro['deportivo_18_de_marzo'] = ['lindavista', 'la_villa_basilica', 'indios_verdes', 'potrero']
metro['la_villa_basilica'] = ['deportivo_18_de_marzo', 'martin_carrera']
metro['martin_carrera'] = ['la_villa_basilica', 'talisman']

# Linea 7
metro['aquiles_serdan'] = ['el_rosario', 'camarones']
metro['camarones'] = ['aquiles_serdan', 'refineria']
metro['refineria'] = ['camarones', 'tacuba']
metro['tacuba'] = ['refineria', 'san_joaquin', 'panteones', 'cuitlahuac']
metro['san_joaquin'] = ['tacuba', 'polanco']
metro['polanco'] = ['san_joaquin', 'auditorio']
metro['auditorio'] = ['polanco', 'constituyentes']
metro['constituyentes'] = ['auditorio', 'tacubaya']
metro['tacubaya'] = ['constituyentes', 'san_pedro_de_los_pinos', 'observatorio', 'patriotismo', 'juanacatlan']
metro['san_pedro_de_los_pinos'] = ['tacubaya', 'san_antonio']
metro['san_antonio'] = ['san_pedro_de_los_pinos', 'mixcoac']
metro['mixcoac'] = ['san_antonio', 'insurgentes_sur', 'barranca_del_muerto']
metro['barranca_del_muerto'] = ['mixcoac']

# Linea 8
metro['doctores'] = ['salto_del_agua', 'obrera']
metro['obrera'] = ['doctores', 'chabacano']
metro['la_viga'] = ['chabacano', 'santa_anita']
metro['coyuya'] = ['santa_anita', 'iztacalco']
metro['iztacalco'] = ['coyuya', 'apatlaco']
metro['apatlaco'] = ['iztacalco', 'aculco']
metro['aculco'] = ['apatlaco', 'escuadron_201']
metro['escuadron_201'] = ['aculco', 'atlalilco']
metro['iztapalapa'] = ['atlalilco', 'cerro_de_la_estrella']
metro['cerro_de_la_estrella'] = ['iztapalapa', 'uam']
metro['uam'] = ['cerro_de_la_estrella', 'constitucion_de_1917']
metro['constitucion_de_1917'] = ['uam']

# Linea 9
metro['patriotismo'] = ['tacubaya', 'chilpancingo']
metro['chilpancingo'] = ['patriotismo', 'centro_medico']
metro['centro_medico'] = ['chilpancingo', 'lazaro_cardenas', 'hospital_general', 'etiopia']
metro['lazaro_cardenas'] = ['centro_medico', 'chabacano']
metro['chabacano'] = ['lazaro_cardenas', 'jamaica', 'san_antonio_abad', 'obrera', 'la_viga', 'viaducto']
metro['jamaica'] = ['chabacano', 'mixiuhca', 'fray_servando', 'santa_anita']
metro['mixiuhca'] = ['jamaica', 'velodromo']
metro['velodromo'] = ['mixiuhca', 'ciudad_deportiva']
metro['ciudad_deportiva'] = ['velodromo', 'puebla']
metro['puebla'] = ['ciudad_deportiva', 'pantitlan']
metro['pantitlan'] = ['puebla', 'zaragoza', 'hangares', 'agricola_oriental']

# Linea 12
metro['insurgentes_sur'] = ['mixcoac', 'hospital_20_de_noviembre']
metro['hospital_20_de_noviembre'] = ['insurgentes_sur', 'zapata']
metro['parque_de_los_venados'] = ['zapata', 'eje_central']
metro['eje_central'] = ['parque_de_los_venados', 'ermita']
metro['mexicaltzingo'] = ['ermita', 'atlalilco']
metro['atlalilco'] = ['mexicaltzingo', 'culhuacan', 'escuadron_201', 'iztapalapa']
metro['culhuacan'] = ['atlalilco', 'san_andres_tomatlan']
metro['san_andres_tomatlan'] = ['culhuacan', 'lomas_estrella']
metro['lomas_estrella'] = ['san_andres_tomatlan', 'calle_11']
metro['calle_11'] = ['lomas_estrella', 'periferico_oriente']
metro['periferico_oriente'] = ['calle_11', 'tezonco']
metro['tezonco'] = ['periferico_oriente', 'olivos']
metro['olivos'] = ['tezonco', 'nopalera']
metro['nopalera'] = ['olivos', 'zapotitlan']
metro['zapotitlan'] = ['nopalera', 'tlaltenco']
metro['tlaltenco'] = ['zapotitlan', 'tlahuac']
metro['tlahuac'] = ['tlaltenco']

# Linea A
metro['agricola_oriental'] = ['pantitlan', 'canal_de_san_juan']
metro['canal_de_san_juan'] = ['agricola_oriental', 'tepalcates']
metro['tepalcates'] = ['canal_de_san_juan', 'guelatao']
metro['guelatao'] = ['tepalcates', 'penon_viejo']
metro['penon_viejo'] = ['guelatao', 'acatitla']
metro['acatitla'] = ['penon_viejo', 'santa_marta']
metro['santa_marta'] = ['acatitla', 'los_reyes']
metro['los_reyes'] = ['santa_marta', 'la_paz']
metro['la_paz'] = ['los_reyes'] 

# Linea B
metro['buenavista'] = ['guerrero']
metro['guerrero'] = ['buenavista', 'garibaldi', 'tlatelolco', 'hidalgo']
metro['garibaldi'] = ['guerrero', 'lagunilla', 'bellas_artes']
metro['lagunilla'] = ['garibaldi', 'tepito']
metro['tepito'] = ['lagunilla', 'morelos']
metro['morelos'] = ['tepito', 'san_lazaro', 'canal_del_norte', 'candelaria']
metro['flores_magon'] = ['san_lazaro', 'romero_rubio']
metro['romero_rubio'] = ['flores_magon', 'oceania']
metro['oceania'] = ['romero_rubio', 'deportivo_oceania', 'aragon', 'terminal_aerea']
metro['deportivo_oceania'] = ['oceania', 'bosque_de_aragon']
metro['bosque_de_aragon'] = ['deportivo_oceania', 'villa_de_aragon']
metro['villa_de_aragon'] = ['bosque_de_aragon', 'nezahualcoyotl']
metro['nezahualcoyotl'] = ['villa_de_aragon', 'impulsora']
metro['impulsora'] = ['nezahualcoyotl', 'rio_de_los_remedios']
metro['rio_de_los_remedios'] = ['impulsora', 'muzquiz']
metro['muzquiz'] = ['rio_de_los_remedios', 'ecatepec']
metro['ecatepec'] = ['muzquiz', 'olimpica']
metro['olimpica'] = ['ecatepec', 'plaza_aragon']
metro['plaza_aragon'] = ['olimpica', 'ciudad_azteca']
metro['ciudad_azteca'] = ['plaza_aragon']


metro_cdmx = {}
for nodo, vecinos in metro.items():
    if nodo not in metro_cdmx:
        metro_cdmx[nodo] = {}
    for vecino in vecinos:
        metro_cdmx[nodo][vecino] = 1
        if vecino not in metro_cdmx:
            metro_cdmx[vecino] = {}
        metro_cdmx[vecino][nodo] = 1

def resolver_ruta(inicio, meta):
    print(f"\n==============================================")
    print(f"Ruta solicitada: {inicio} -> {meta}")
    print(f"==============================================")
    
    problema = GraphProblem(inicio, meta, metro_cdmx)
    
    # Búsqueda en Profundidad (DFS)
    resultado_dfs = depth_first_graph_search(problema)
    if resultado_dfs:
        ruta = resultado_dfs.path()
        print(f"\n DFS (Profundidad) encontró ruta con {len(ruta)-1} estaciones recorridas:")
        print(" -> ".join(ruta))
    
    # Búsqueda en Anchura (BFS)
    resultado_bfs = breadth_first_graph_search(problema)
    if resultado_bfs:
        ruta = resultado_bfs.path()
        print(f"\n BFS (Anchura) encontró la ruta ÓPTIMA con {len(ruta)-1} estaciones recorridas:")
        print(" -> ".join(ruta))

if __name__ == "__main__":
    
    # 1. Cuatro Caminos -> Pantitlan
    resolver_ruta("cuatro_caminos", "pantitlan")

    # 2. Politécnico -> Taxqueña
    resolver_ruta("politecnico", "tasquena")

    # 3. Zapata -> Oceania
    resolver_ruta("zapata", "oceania")