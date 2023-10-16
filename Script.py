from random import choice # importando a função "choice" da biblioteca "random"
from time import sleep # importando a função "sleep" da biblioteca "time"

#criando uma lista dos numeros de 1 a 60
lista = list(range(1, 61)) 

# função para gerar números aleatorios
def gerarNumeros():

    #criando uma lista para armazenar os numeros gerados
    listaDeNumeros = []

    #loop para gerar e adicionar os numeros na lista
    #esse loop vai pegar um dos 60 numeros de 'lista' e vai adicionar em 'listaDeNumeros'
    #isso vai se repetir até gerar e adicionar 6 numeros aleatórios
    for c in range(1, 7):
        numeroGerado = choice(lista) # escolhendo um dos 60 
        listaDeNumeros.append(numeroGerado) #adicionando a lista
    
    #retornando a lista de numeros
    return listaDeNumeros

#copiando os valores de 'listaDeNumeros' para 'numeros_sorteados' por meio da função acima
numeros_sorteados = list(gerarNumeros())

#variavel para armazenar a quantidade de acertos
acertos = 0

#lista para armazenar os numeros jogados pelo usuario
jogadas = []

#loop para pegar os numeros jogados pelo usuario
#irá se repetir 6 vezes 
for i in range(1, 7):
    jogada = int(input(f"entre com a sua {i}º jogada:\n")) #pegando os dados do usuario
    jogadas.append(jogada) #adicionando os dados na lista 'jogadas'

#loop para verificar a quantidade de acertos
for c in range(0, 6):
    #esse if verifica se os numeros sorteados estão iguais aos numeros inseridos pelo jogador
    if numeros_sorteados[c] == jogadas[c]:
        acertos += 1

#mostrando o resultado do jogo
print("gerando resultados...")
sleep(1)
if acertos == 6:
    print("parabens, você acertou todos os números")
    print(f"quantidade de acertos: {acertos}")
else:
    print(f"você acertou {acertos} numeros")

#carai me senti um profissional comentando essa porra