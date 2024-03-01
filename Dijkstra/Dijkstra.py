from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if self.existe_vertice(self.get_vertice(V)):
            ind = self.indice_do_vertice(self.get_vertice(V))
            lin = self.arestas[ind]
            rotulos = []

            for i in lin:
                matriz_adj = i
                for j in matriz_adj:
                    rotulos.append(j)
            return rotulos
        else:
            raise VerticeInvalidoError("Vertice Inválido")

    def dijkstra(self,a,b):

        #Verificação de erro caso os vertices nao existam
        if not self.existe_vertice(self.get_vertice(a)) or not self.existe_vertice(self.get_vertice(b)):
            raise VerticeInvalidoError(
                "Um dos Vertices passados é inexistente no grafo."
            )

        #Geração de equivalentes a PI e Beta
        predecessor = {}
        custo = {}

        for v in self.vertices:
            predecessor[v.rotulo] = ""
            custo[v.rotulo] = float("inf")

        custo[a] = 0

        predecessor = self.dijkstra_rec(a,b,a,predecessor,custo)

        #Verificação de erro caso nao exista caminho entre os vertices
        #Nesse caso o predecessor continua uma string vazia como gerada acima
        if predecessor[b] == "":
            raise KeyError(
                "Não existe caminho entre os vértices."
            )

        #Ao fim da recursão teremos um dicionário de rotulos de vertices
        #Portanto, transformaremos aqui em lista para retornar para o teste
        caminho = []
        caminho.append(b)
        while predecessor[b] != "":
            caminho.append(predecessor[b])
            b = predecessor[b]

        return caminho[::-1]

    def dijkstra_rec(self,a,b,atual,predecessor,custo):
        # Ordenação de arestas por peso
        arestas = sorted(self.arestas_sobre_vertice(atual), key=lambda rotulo:self.get_aresta(rotulo).peso)

        # Transformando os rotulos em objetos
        arestas =[self.get_aresta(aresta) for aresta in arestas]

        # Percorrendo as arestas e fazendo os calculos do algoritmo de dijkstra
        for aresta in arestas:
            soma = aresta.peso + custo[atual]
            # Ponto importante, aqui definimos o grafo de maneira direcionada
            proximo = aresta.v2.rotulo if atual == aresta.v1.rotulo else aresta.v1.rotulo
            if soma < custo[proximo]:
                custo[proximo] = soma
                predecessor[proximo] = atual
                return self.dijkstra_rec(a, b, proximo, predecessor, custo)


        # Regressando os vertices
        if atual != a:
            atual = predecessor[atual]
            return self.dijkstra_rec(a, b, atual, predecessor, custo)

        return predecessor