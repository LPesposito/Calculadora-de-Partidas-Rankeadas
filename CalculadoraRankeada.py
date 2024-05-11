vitorias = int(input("Insira a quantidade de vitórias: "))
derrotas = int(input("Insira a quantidade de derrotas: "))

def calcularRank(vitorias:int,derrotas:int) -> str:
    pontos_de_rank = vitorias - derrotas
    nivel:str
    if pontos_de_rank <=10 :
        nivel = "Ferro"
    elif pontos_de_rank in range(11,20):
        nivel = "Bronze"
    elif pontos_de_rank in range(21,50):
        nivel = "Prata"
    elif pontos_de_rank in range(51,80):
        nivel = "Ouro"
    elif pontos_de_rank in range(81,90):
        nivel = "Diamante"
    elif pontos_de_rank in range(91,101):
        nivel = "Lendário"
    elif pontos_de_rank >= 101:
        nivel = "Imortal"
    
    print(f"O Herói tem saldo de {vitorias} está no nível de {nivel}")

calcularRank(vitorias,derrotas)        
        
## Objetivo:

#Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"