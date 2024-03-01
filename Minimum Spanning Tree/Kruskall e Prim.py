from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
import copy


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_vertice(self.get_vertice(V)):
            raise VerticeInvalidoError("Verticie não existe")

        resultado = set()
        index_vertice = self.indice_do_vertice(self.get_vertice(V))
        for i in range(len(self.vertices)):
            for aresta in self.arestas[index_vertice][i]:
                resultado.add(aresta)
        return resultado

    def Fila_prioridade_prim(self, l_vertices):
        arestas = []
        for vertice in l_vertices:
            arestas += [self.get_aresta(aresta)
                        for aresta in self.arestas_sobre_vertice(vertice.rotulo)]
        arestas.sort(key=lambda aresta: aresta.peso)
        for aresta in arestas:
            vertices_mst = [vertice.rotulo for vertice in l_vertices]
            if (aresta.v1.rotulo in vertices_mst and aresta.v2.rotulo not in vertices_mst) or (
                    aresta.v2.rotulo in vertices_mst and aresta.v1.rotulo not in vertices_mst):
                return aresta
        return False

    def Prim(self):
        mst = MeuGrafo()
        vertice_inicial = self.vertices[0].rotulo
        mst.adiciona_vertice(vertice_inicial)
        while (len(self.vertices) != len(mst.vertices)):
            aresta = self.Fila_prioridade_prim(mst.vertices)
            if aresta:
                if not mst.get_vertice(aresta.v1.rotulo):
                    mst.adiciona_vertice(aresta.v1.rotulo)
                if not mst.get_vertice(aresta.v2.rotulo):
                    mst.adiciona_vertice(aresta.v2.rotulo)
                mst.adiciona_aresta(
                    aresta.rotulo, aresta.v1.rotulo, aresta.v2.rotulo, aresta.peso)
        return mst

    def Fila_prioridade_kruskall(self):
        arestas = []
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                for key in self.arestas[i][j]:
                    arestas.append(self.arestas[i][j][key])

        arestas.sort(key=lambda aresta: aresta.peso)
        return arestas

    def esta_em_outra_arvore(self, sets, v1, v2):
        for set in sets:
            if v1 in set and v2 in set:
                return False
        return True

    def Agrupar_arvores(self, subconjuntos, v1, v2):
        nova_floresta = []
        vertices = []
        for subconjunto in subconjuntos:
            if v1 not in subconjunto and v2 not in subconjunto:
                nova_floresta.append(subconjunto)
            else:
                vertices += [vertice for vertice in subconjunto]
        nova_floresta.append(set(vertices))
        return nova_floresta

    def adicionar_a_mst(self, mst, v1, v2, edge):
        if v1 not in mst.vertices:
            mst.adiciona_vertice(v1.rotulo)
        if v2 not in mst.vertices:
            mst.adiciona_vertice(v2.rotulo)
        mst.adiciona_aresta(edge, v1.rotulo, v2.rotulo)

    def gerar_floresta(self):
        return [set(vertex.rotulo) for vertex in self.vertices]

    def kruskall(self):
        mst = MeuGrafo()
        arestas = self.Fila_prioridade_kruskall()
        subconjuntos_mst = self.gerar_floresta()

        for aresta in arestas:
            if self.esta_em_outra_arvore(subconjuntos_mst, aresta.v1.rotulo, aresta.v2.rotulo):
                subconjuntos_mst = self.Agrupar_arvores(
                    subconjuntos_mst, aresta.v1.rotulo, aresta.v2.rotulo)
                self.adicionar_a_mst(mst, aresta.v1, aresta.v2, aresta.rotulo)
        return mst

    def display(self):
        result = set()
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                for aresta in self.arestas[i][j]:
                    result.add(
                        f'{self.vertices[i].rotulo} - {aresta} - {self.vertices[j].rotulo}')
        return result