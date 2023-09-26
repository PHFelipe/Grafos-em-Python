from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        vna = set()
        for v in self.vertices:
            va = []
            for a in self.arestas:
                if self.arestas[a].v2.rotulo == v.rotulo:
                    v1 = self.arestas[a].v1.rotulo
                    va.append(v1)
                elif self.arestas[a].v1.rotulo == v.rotulo:
                    v2 = self.arestas[a].v2.rotulo
                    va.append(v2)
            for vt in self.vertices:
                if vt.rotulo != v.rotulo and vt.rotulo not in va:
                    if f'{vt}-{v.rotulo}' not in vna:
                        vna.add(f'{v.rotulo}-{vt}')
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == self.arestas[a].v2.rotulo:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_vertice(self.get_vertice(V)):
            raise VerticeInvalidoError()
        else:
            g = 0
            for a in self.arestas:
                if self.arestas[a].v1.rotulo == V:
                    g += 1
                if self.arestas[a].v2.rotulo == V:
                    g += 1
            return g

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        ca = []
        for a in self.arestas:
            ar = (self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo)
            if ar in ca or ar[::-1] in ca:
                return True
            else:
                ca.append(ar)
        return False

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

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_paralelas() or self.ha_laco():
            return False
        else:
            c = len(self.vertices) - 1
            v = self.vertices
            for x in v:
                if self.grau(x.rotulo) != c:
                    return False
            return True