# Função para calcular saldo e determinar o nível
def calculadora_rankeadas(vitorias, derrotas):
    # Calculando o saldo de partidas
    saldo_vitorias = vitorias - derrotas

    # Determinando o nível do jogador
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # Retornando os resultados
    return saldo_vitorias, nivel

# Entrada de dados
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

# Chamando a função
saldo, nivel = calculadora_rankeadas(vitorias, derrotas)

# Exibindo a saída
print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}.")
