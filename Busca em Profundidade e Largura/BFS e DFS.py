from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_vertice(self.get_vertice(V)):
            raise VerticeInvalidoError()
        else:
            asv = set()
            for a in self.arestas:
                if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                    asv.add(self.arestas[a].rotulo)
            return asv


    def dfs(self, raiz=''):
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(raiz)

        def dfs_rec(v: str, arvore_dfs: MeuGrafo):
            adj = list(self.arestas_sobre_vertice(v))
            adj.sort()
            for a in adj:
                aresta = self._arestas[a]
                proximo = aresta.v2 if aresta.v1.rotulo == v else aresta.v1
                if not arvore_dfs.existe_rotulo_vertice(proximo.rotulo):
                    arvore_dfs.adiciona_vertice(proximo.rotulo)
                    arvore_dfs.adiciona_aresta(aresta.rotulo, aresta.v1.rotulo, aresta.v2.rotulo)
                    print(arvore_dfs)
                    dfs_rec(proximo.rotulo, arvore_dfs)

            return arvore_dfs

        return dfs_rec(raiz, arvore_dfs)

    def bfs(self,raiz=''):
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(raiz)

        def bfs_rec(v,arvore_bfs):
            adj = list(self.arestas_sobre_vertice(v))
            adj.sort()
            vertices = []
            for a in adj:
                aresta = self._arestas[a]
                proximo = aresta.v2 if aresta.v1.rotulo == v else aresta.v1
                if not arvore_bfs.existe_rotulo_vertice(proximo.rotulo):
                    vertices.append(proximo)
                    arvore_bfs.adiciona_vertice(proximo.rotulo)
                    arvore_bfs.adiciona_aresta(aresta.rotulo,aresta.v1.rotulo,aresta.v2.rotulo)
                    print(arvore_bfs)
            for v in vertices: bfs_rec(v.rotulo,arvore_bfs)
            return arvore_bfs

        return bfs_rec(raiz,arvore_bfs)