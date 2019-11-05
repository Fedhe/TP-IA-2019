# coding: utf-8
#Imports
from simpleai.search import breadth_first, SearchProblem, astar, greedy, depth_first
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer

 
##Estado inicial para pruebas aparte
##Primer tupla de tuplas son barcos piratas, segunda franceses.
##Los piratas tienen el nombre ('A', 'B'..), fila, columna, si tiene o no mapa (0 o 1) y si esta hundido o no (0 o 1)
INITIAL = ((('A', 4, 4, 0, 0), ('B', 4, 5, 0, 0), ('C', 5, 4, 0, 0)), ((0, 2), (0, 3), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (5, 0)))


def tuple2list(t):
    return [list(row) for row in t]


def list2tuple(t):
    return tuple(tuple(row) for row in t)

class Barcos_Piratas(SearchProblem):
    #Costo devuelve 1 por cada acción
    def cost(self, state1, action, state2):
        return 1
 
    def is_goal(self, state):
        #Si alguno de los barcos piratas tiene el mapa y además éste esta en la isla pirata es meta
        for barco in state[0]:
            fila_barco = barco[1]
            columna_barco = barco[2]
            if (fila_barco, columna_barco) == (5, 5) and barco[3] == 1:
                return True

        return False
 
    def actions(self, state):
        listactions=[]
        total = 0
        #Si no están todos hundidos hay acciones disponibles..
        for barcos in state[0]:
            if barcos[4] == 1:
                total = total + 1
        
        if not total == len(state[0]):
            for barco in state[0]:
                #Si está hundido no agrego ninguna accion
                if barco[4] != 1:
                    nombre, fila, columna, mapa, hundido = barco

                    if fila != 0:
                        listactions.append('Mover-Arriba-Barco-' + str(nombre))

                    if fila != 5:
                        listactions.append('Mover-Abajo-Barco-' + str(nombre))

                    if columna != 0:
                        listactions.append('Mover-Izquierda-Barco-' + str(nombre))

                    if columna != 5:
                        listactions.append('Mover-Derecha-Barco-' + str(nombre))

            return listactions

        else:
            return listactions
 
    def result(self, state, action):
        state = tuple2list(state)

        if action == 'Mover-Abajo-Barco-A':
            state[0][0] = list(state[0][0])
            state[0][0][1] = state[0][0][1] + 1
            state[0][0] = tuple(state[0][0])
            indice = 0

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                state[0][0] = list(state[0][0])
                state[0][0][4] = 1
                state[0][0] = tuple(state[0][0])
                #state[0].remove(state[0][indice])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Arriba-Barco-A':
            state[0][0] = list(state[0][0])
            state[0][0][1] = state[0][0][1] - 1
            state[0][0] = tuple(state[0][0])
            indice = 0

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][0] = list(state[0][0])
                state[0][0][4] = 1
                state[0][0] = tuple(state[0][0])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Izquierda-Barco-A':
            state[0][0] = list(state[0][0])
            state[0][0][2] = state[0][0][2] - 1
            state[0][0] = tuple(state[0][0])
            indice = 0

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][0] = list(state[0][0])
                state[0][0][4] = 1
                state[0][0] = tuple(state[0][0])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Derecha-Barco-A':
            state[0][0] = list(state[0][0])
            state[0][0][2] = state[0][0][2] + 1
            state[0][0] = tuple(state[0][0])
            indice = 0

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][0] = list(state[0][0])
                state[0][0][4] = 1
                state[0][0] = tuple(state[0][0])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Abajo-Barco-B':
            for tupla in state[0]:
                if 'B' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][1] = state[0][indice][1] + 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][1] = list(state[0][1])
                state[0][1][4] = 1
                state[0][1] = tuple(state[0][1])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state
        
        if action == 'Mover-Arriba-Barco-B':
            for tupla in state[0]:
                if 'B' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][1] = state[0][indice][1] - 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][1] = list(state[0][1])
                state[0][1][4] = 1
                state[0][1] = tuple(state[0][1])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Izquierda-Barco-B':
            for tupla in state[0]:
                if 'B' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][2] = state[0][indice][2] - 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][1] = list(state[0][1])
                state[0][1][4] = 1
                state[0][1] = tuple(state[0][1])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Derecha-Barco-B':
            for tupla in state[0]:
                if 'B' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][2] = state[0][indice][2] + 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][1] = list(state[0][1])
                state[0][1][4] = 1
                state[0][1] = tuple(state[0][1])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Abajo-Barco-C':
            for tupla in state[0]:
                if 'C' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][1] = state[0][indice][1] + 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][2] = list(state[0][2])
                state[0][2][4] = 1
                state[0][2] = tuple(state[0][2])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state
        
        if action == 'Mover-Arriba-Barco-C':
            for tupla in state[0]:
                if 'C' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][1] = state[0][indice][1] - 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][2] = list(state[0][2])
                state[0][2][4] = 1
                state[0][2] = tuple(state[0][2])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Izquierda-Barco-C':
            for tupla in state[0]:
                if 'C' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][2] = state[0][indice][2] - 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][2] = list(state[0][2])
                state[0][2][4] = 1
                state[0][2] = tuple(state[0][2])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        if action == 'Mover-Derecha-Barco-C':
            for tupla in state[0]:
                if 'C' in tupla:
                    indice = state[0].index(tupla)
                    state[0][indice] = list(state[0][indice])
                    state[0][indice][2] = state[0][indice][2] + 1
                    state[0][indice] = tuple(state[0][indice])

            #Si llegó a la isla, copia el mapa
            if (state[0][indice][1], state[0][indice][2]) == (2, 0):
                state[0][indice] = list(state[0][indice])
                state[0][indice][3] = 1
                state[0][indice] = tuple(state[0][indice])

            #Si llegó donde hay un francés, se hunde
            if (state[0][indice][1], state[0][indice][2]) in state[1]:
                fila = state[0][indice][1]
                columna = state[0][indice][2]
                #state[0].remove(state[0][indice])
                state[0][2] = list(state[0][2])
                state[0][2][4] = 1
                state[0][2] = tuple(state[0][2])
                state[1].remove((fila, columna))
            state = list2tuple(state)
            return state

        state = list2tuple(state)
        return state
        

    def heuristic(self, state):
        costo = 0
        distancia = 0
        distancias = []
        for barco in state[0]:
            #Para cada barco, si no está hundido calculo distancia..
            if barco[4] != 1:
                if barco[3] != 1:
                    distancia = (abs(2 - barco[1]) + abs (0 - barco[2]) + abs(2 - 5) + abs(0 - 5))
                    distancias.append(distancia)
                    
                else:
                    distancia = (abs(5 - barco[1]) + abs(5 - barco[2]))
                    distancias.append(distancia)

        #Si se cargaron distancias, ordeno de menor a mayor y tomo la menor.
        if distancias != []:
            distancias.sort()
            costo = distancias[0]
        
        return costo


def resolver(metodo_busqueda, franceses, piratas):
    viewer = None
    letra = 0
    franceses = list(franceses)
    piratas = list(piratas)
    for barcos in piratas:
        if letra == 0:
            piratas[0] = list(piratas[0])
            piratas[0].insert(0, 'A')
            piratas[0].append(0)
            piratas[0].append(0)
            piratas[0] = tuple(piratas[0])

        if letra == 1:
            piratas[1] = list(piratas[1])
            piratas[1].insert(0, 'B')
            piratas[1].append(0)
            piratas[1].append(0)
            piratas[1] = tuple(piratas[1])

        if letra == 2:
            piratas[2] = list(piratas[2])
            piratas[2].insert(0, 'C')
            piratas[2].append(0)
            piratas[2].append(0)
            piratas[2] = tuple(piratas[2])
        letra = letra + 1
    
    estado = ((tuple(piratas), tuple(franceses)))
    
    problem = Barcos_Piratas(estado)

    if metodo_busqueda == "breadth_first":    
        resultado = breadth_first(problem, graph_search=True, viewer = viewer)
    elif metodo_busqueda == "greedy":    
        resultado = greedy(problem, graph_search=True, viewer = viewer)
    elif metodo_busqueda == "depth_first":    
        resultado = depth_first(problem, graph_search=True, viewer = viewer)
    elif metodo_busqueda == "astar":
        resultado = astar(problem, graph_search=True, viewer = viewer)
    elif metodo_busqueda == "uniform_cost":
        resultado = uniform_cost(problem, graph_search=True, viewer = viewer)

    return resultado
    
if __name__ == '__main__':

    visor = WebViewer()
    visor = BaseViewer()
##    visor = None
    result = depth_first(Barcos_Piratas(INITIAL),viewer=visor, graph_search=True)
    
    print (result.state)
    print (result.path())
    print (len(result.path()))
    print (result.cost)
    print (visor.stats)
