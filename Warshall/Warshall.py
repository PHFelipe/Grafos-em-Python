from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):


    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        E = deepcopy(self.arestas)
        vertices = self.vertices
        tamanho = len(vertices)
        for i in range(tamanho):
            for j in range(tamanho):
                if len(E[j][i])>0:
                    E[j][i] = 1
                else:
                    E[j][i] = 0
        for i in range(tamanho):
            for j in range(tamanho):
                if E[j][i] == 1:
                    for k in range(tamanho):
                        E[j][k] = max((E[j][k],E[i][k]))
        return E