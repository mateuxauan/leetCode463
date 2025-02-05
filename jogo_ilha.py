import random

n=int(input("A matriz será de quanto por quanto ?"))
q=int(input("quantos quadrados a ilha deve ocupar?"))



def criaJogo(n,q):
    # criar uma matriz de tamano n por n
    matriz = [ [0]*n for _ in range(n)]
    # Garantir que q seja menor que n² (quantidade total de posições na matriz)
    q = min(q, n * n - 1)
    # Criar lista com todas as posições possíveis dentro da matriz
    posicoes_validas = [(i, j) for i in range(n) for j in range(n)]
    # Selecionar q posições únicas aleatórias
    posicoes_selecionadas = random.sample(posicoes_validas, q)
    # Preencher as posições selecionadas com 1
    for i, j in posicoes_selecionadas:
        matriz[i][j] = 1
       
    return matriz    
 
matriz=criaJogo(n,q)
print(matriz)

def imprimeMatriz(matriz):
    for linha in matriz:
        print(" ".join(str(elem) for elem in linha))

imprimeMatriz(matriz)

def areaMatriz(matriz):
    contador = 0
    for linha in matriz:
        contador += linha.count(1)  # Conta os 1s em cada linha e soma ao total
    return contador

area = areaMatriz(matriz)
print(f"A area da matriz é: {area}")

P=area*4

def perimetroMatriz(matriz):
    n = len(matriz)
    conexoes = 0  # Contador de conexões

    for l in range(n):
        for c in range(n):
            if matriz[l][c] == 1:
                # Verifica se há conexão acima
                if l > 0 and matriz[l- 1][c] == 1:
                    conexoes += 1
                # Verifica se há conexão à esquerda
                if c > 0 and matriz[l][c - 1] == 1:
                    conexoes += 1

    return conexoes

conexoes=perimetroMatriz(matriz)

perimetro = P - 2*conexoes

print(f"o perimetro da sua ilha é {perimetro}")




    
