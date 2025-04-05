import networkx as nx
import random
import time
import matplotlib.pyplot as plt

# ------------------ Algoritmos de coloração ------------------

def colorir_com_k_cores(grafo, k):
    cores = {}

    def cor_segura(vertice, cor):
        for vizinho in grafo.neighbors(vertice):
            if vizinho in cores and cores[vizinho] == cor:
                return False
        return True

    def backtrack(lista_vertices, i):
        if i == len(lista_vertices):
            return True
        vertice = lista_vertices[i]
        for cor in range(k):
            if cor_segura(vertice, cor):
                cores[vertice] = cor
                if backtrack(lista_vertices, i + 1):
                    return True
                del cores[vertice]
        return False

    if backtrack(list(grafo.nodes), 0):
        return cores
    else:
        return False

def colorir_guloso(grafo):
    cores = {}
    for vertice in grafo.nodes:
        usadas = {cores[v] for v in grafo.neighbors(vertice) if v in cores}
        for cor in range(len(grafo)):
            if cor not in usadas:
                cores[vertice] = cor
                break
    return cores

def colorir_guloso_ordenado(grafo):
    vertices_ordenados = sorted(grafo.nodes, key=lambda v: grafo.degree[v], reverse=True)
    cores = {}
    for vertice in vertices_ordenados:
        usadas = {cores[v] for v in grafo.neighbors(vertice) if v in cores}
        for cor in range(len(grafo)):
            if cor not in usadas:
                cores[vertice] = cor
                break
    return cores

# ------------------ Funções de Teste e Visualização ------------------

def gerar_grafo_aleatorio(num_vertices, prob_arestas):
    return nx.erdos_renyi_graph(num_vertices, prob_arestas)

def verificar_coloração_valida(grafo, cores):
    for u, v in grafo.edges:
        if cores[u] == cores[v]:
            return False
    return True

def mostrar_grafo(grafo, cores, titulo="Grafo Colorido"):
    pos = nx.spring_layout(grafo, seed=42)
    cores_nos = [cores[n] for n in grafo.nodes]
    cmap = plt.cm.get_cmap('tab10', max(cores_nos) + 1)

    plt.figure(figsize=(6, 5))
    nx.draw_networkx(
        grafo, pos,
        node_color=cores_nos,
        with_labels=True,
        node_size=500,
        font_color='white',
        cmap=cmap,
        font_weight='bold'
    )
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def testar_algoritmos(num_testes=5, num_vertices=8, prob_arestas=0.5):
    for i in range(num_testes):
        print(f"\n🧪 Teste {i+1}")
        grafo = gerar_grafo_aleatorio(num_vertices, prob_arestas)
        print(f"Nós: {len(grafo.nodes)} | Arestas: {len(grafo.edges)}")
        print("-" * 40)

        # Exato
        k = num_vertices
        inicio = time.time()
        resultado_exato = colorir_com_k_cores(grafo, k)
        tempo_exato = time.time() - inicio

        if resultado_exato:
            valido_exato = verificar_coloração_valida(grafo, resultado_exato)
            cores_usadas_exato = len(set(resultado_exato.values()))
        else:
            valido_exato = False
            cores_usadas_exato = None

        print(f"🎯 Exato      | Cores: {cores_usadas_exato} | Válido: {valido_exato} | Tempo: {tempo_exato:.4f}s")

        # Guloso
        inicio = time.time()
        resultado_guloso = colorir_guloso(grafo)
        tempo_guloso = time.time() - inicio

        valido_guloso = verificar_coloração_valida(grafo, resultado_guloso)
        cores_usadas_guloso = len(set(resultado_guloso.values()))
        print(f"⚡ Guloso     | Cores: {cores_usadas_guloso} | Válido: {valido_guloso} | Tempo: {tempo_guloso:.4f}s")

        # Guloso ordenado
        inicio = time.time()
        resultado_ordenado = colorir_guloso_ordenado(grafo)
        tempo_ordenado = time.time() - inicio

        valido_ordenado = verificar_coloração_valida(grafo, resultado_ordenado)
        cores_usadas_ordenado = len(set(resultado_ordenado.values()))
        print(f"📊 Ordenado   | Cores: {cores_usadas_ordenado} | Válido: {valido_ordenado} | Tempo: {tempo_ordenado:.4f}s")

        # Mostrar graficamente apenas no primeiro teste
        if i == 0:
            if resultado_exato:
                mostrar_grafo(grafo, resultado_exato, "🎯 Coloração Exata")
            mostrar_grafo(grafo, resultado_guloso, "⚡ Coloração Gulosa")
            mostrar_grafo(grafo, resultado_ordenado, "📊 Coloração Ordenada")

# ------------------ Executar testes ------------------

if __name__ == "__main__":
    testar_algoritmos(num_testes=5, num_vertices=8, prob_arestas=0.5)









