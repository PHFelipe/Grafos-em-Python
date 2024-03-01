from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def aresta_sobre_vertice_direcionado(self,V):
        vertice = self.get_vertice(V)
        if self.existe_vertice(vertice):
            arestas_incidentes = list()

            for linha in self.arestas[self.indice_do_vertice(vertice)]:
                for aresta in linha:
                    arestas_incidentes.append(aresta)

            return set(arestas_incidentes)
        else:
            raise VerticeInvalidoError("O vértice não existe no grafo")

    def bellman_ford(self, a, b):
        if not self.existe_vertice(self.get_vertice(a)) or not self.existe_vertice(self.get_vertice(b)):
            raise VerticeInvalidoError(
                "Um dos Vertices passados é inexistente no grafo."
            )

        predecessor = {}
        custo = {}

        for v in self.vertices:
            predecessor[v.rotulo] = ""
            custo[v.rotulo] = float("inf")

        custo[a] = 0
        # O algoritmo vai rodar até N (Onde N é o número de vertices)
        for i in range(len(self.vertices) - 1):
            #Percorrendo os vertices e analisando as arestas sobre aquele vertice
            for v in self.vertices:
                arestas = sorted(self.aresta_sobre_vertice_direcionado(v.rotulo), key=lambda rotulo:self.get_aresta(rotulo).peso)
                arestas = [self.get_aresta(aresta) for aresta in arestas]
                # percorrendo as arestas sobre aquele vertice
                for aresta in arestas:
                    soma = aresta.peso + custo[v.rotulo]
                    proximo = aresta.v2.rotulo if v.rotulo == aresta.v1.rotulo else aresta.v1.rotulo
                    if soma < custo[proximo]:
                        custo[proximo] = soma
                        predecessor[proximo] = v.rotulo

        for v in self.vertices:
            arestas = sorted(self.aresta_sobre_vertice_direcionado(v.rotulo), key=lambda rotulo: self.get_aresta(rotulo).peso)
            arestas = [self.get_aresta(aresta) for aresta in arestas]
            for aresta in arestas:
                soma = aresta.peso + custo[v.rotulo]
                proximo = aresta.v2.rotulo if v.rotulo == aresta.v1.rotulo else aresta.v1.rotulo
                #caminho de ciclo negativo
                if soma < custo[proximo]:
                    return False

        if predecessor[b] == "":
            raise KeyError(
                "Não existe caminho entre os vértices."
            )
        caminho = []
        caminho.append(b)
        while predecessor[b] != "":
            caminho.append(predecessor[b])
            b = predecessor[b]
        return caminho[::-1]