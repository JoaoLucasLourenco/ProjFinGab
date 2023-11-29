import time
import random
def criar_vetor(tamanho):
  return [random.randint(1, 1000) for _ in range(tamanho)]
#A biblioteca time é utilizada para medir o tempo de execução dos métodos de ordenação.
# Função de ordenação por inserção
#primeiramente criamos um função com o nome Ordenação_inserç
def ordenacao_insercao(vetor):
    # Obtém o comprimento do vetor
    n = len(vetor) 
    # Loop começa a partir do segundo elemento
    for i in range(1, n):
        # Armazena o elemento atual em X
        x = vetor[i]
        # Inicializa j com o índice anterior ao elemento atual
        j = i - 1
        # Move elementos maiores para a direita até encontrar a posição correta para X
        while j >= 0 and x < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        # Insere a chave na posição correta
        vetor[j + 1] = x
# Função de ordenação por seleção
def ordenacao_selecao(vetor):
    # Obtém o comprimento do vetor
    n = len(vetor)
    # Loop percorre o vetor
    for i in range(n): # percorre o vetor do primeiro numero nao ordenado
        # Inicializa o índice do menor numero como o índice atual
        min = i
        # Loop encontra o índice do menor numero não ordenado
        for j in range(i + 1, n): #percorre os elementos  restante do vetor a partir da possição i+1 ja que i ja esta ordenado
            if vetor[j] < vetor[min]: #verifica se o vetor j e menor que o min ,se sim min recebe j 
                min = j
        # Troca o menor elemento com o primeiro numero não ordenado
        vetor[i], vetor[min] = vetor[min], vetor[i]

def ordenacao_bolha(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1): # -1 é eseencial pois compara os elementos do lado.
            if vetor[j] > vetor[j + 1]: # nao ultrapassar  os limites do vetor , se caso não sub -1 o j+1 serie igual a n-1 e poderia ultrapassar o vetor
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def exibir_resultado(tempo_inicio, tempo_fim, vetor_ordenado, metodo):
    print(f"\nOrdenação por {metodo}: {tempo_fim - tempo_inicio:.8f} segundos")
    print(f"Vetor ordenado por {metodo}: {vetor_ordenado}") # Esta função exibe os resultados da ordenação, incluindo o tempo gasto e o vetor ordenado.

def main():
    entrada_usuario = int(input("Entre com o tamanho do vetor: "))
    vetor_desordenado = criar_vetor(entrada_usuario) #não há um número máximo definido para o vetor. O tamanho do vetor é determinado pela entrada do usuário:
    
    print(f"\nVetor Desordenado: {vetor_desordenado}")
    while True:
        try:
            opcao = int(input("\nEscolha o método de ordenação:\n"
                              "1. Inserção Direta\n"
                              "2. Seleção Direta\n"
                              "3. Bolha\n"
                              "Digite um número de acordo a ordenação desejada: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido para escolher o método de ordenação.")
            return
        if opcao == 1:
            vetor_ordenacao = vetor_desordenado.copy()
            tempo_inicio = time.time()
            ordenacao_insercao(vetor_ordenacao)
            tempo_fim = time.time()
            exibir_resultado(tempo_inicio, tempo_fim, vetor_ordenacao, "Inserção Direta")
        elif opcao == 2:
            vetor_ordenacao = vetor_desordenado.copy()
            tempo_inicio = time.time()
            ordenacao_selecao(vetor_ordenacao)
            tempo_fim = time.time()
            exibir_resultado(tempo_inicio, tempo_fim, vetor_ordenacao, "Seleção Direta")
        elif opcao == 3:
            vetor_ordenacao = vetor_desordenado.copy()
            tempo_inicio = time.time()
            ordenacao_bolha(vetor_ordenacao)
            tempo_fim = time.time()
            exibir_resultado(tempo_inicio, tempo_fim, vetor_ordenacao, "Bolha")
        else:
            print("Opção inválida. Por favor, escolha um método válido.")
            continue
        continuar = input("Deseja realizar outra ordenação? (Digite 's' para Sim, ou 'n' para Não): ")
        if continuar.lower() != 's':
            break
if __name__ == "__main__":
    main()
