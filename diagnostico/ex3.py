"""Frequência de palavras: dado um texto, conte quantas vezes cada palavra aparece,
 ignorando maiúsculas e pontuação, e mostre as 3 mais frequentes.
 Por exemplo, para "O gato viu o rato. O rato fugiu!", o resultado esperado é algo
   como o: 3, rato: 2 e uma das palavras que aparecem 1 vez."""

# Importa o módulo "string", que traz uma lista pronta de sinais de pontuação
import string

# Guarda o texto que vamos analisar numa variável
texto = "O gato viu o rato. O rato fugiu!"

# Deixa tudo em minúsculo, para "O" e "o" contarem como a mesma palavra
texto = texto.lower()

# Percorre cada sinal de pontuação (. , ! ? ; : etc.), um de cada vez
for sinal in string.punctuation:
    # Troca o sinal por nada (""), ou seja, apaga ele do texto
    texto = texto.replace(sinal, "")

# Corta o texto nos espaços e cria uma lista com as palavras
# Ex.: ["o", "gato", "viu", "o", "rato", "o", "rato", "fugiu"]
palavras = texto.split()

# Cria um dicionário vazio, onde a chave será a palavra e o valor, quantas vezes ela apareceu
contagem = {}

# Percorre a lista de palavras, uma por vez
for palavra in palavras:
    # contagem.get(palavra, 0) devolve quantas vezes a palavra já apareceu (ou 0, se for a primeira vez)
    # Somamos 1 e guardamos o novo valor no dicionário
    contagem[palavra] = contagem.get(palavra, 0) + 1

# contagem.items() transforma o dicionário em pares (palavra, quantidade)
# sorted(...) ordena esses pares:
#   key=lambda item: item[1] -> ordena pela quantidade (posição 1 do par)
#   reverse=True             -> do maior para o menor
# [:3] pega apenas os 3 primeiros da lista ordenada
mais_frequentes = sorted(contagem.items(), key=lambda item: item[1], reverse=True)[:3]

# Percorre os 3 pares e separa cada um em duas variáveis: palavra e quantidade
for palavra, quantidade in mais_frequentes:
    # Mostra na tela no formato "palavra: quantidade"
    print(f"{palavra}: {quantidade}")