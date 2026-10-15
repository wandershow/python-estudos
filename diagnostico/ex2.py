"""Estatísticas: escreva uma função que receba uma lista de números e retorne um dicionário com minimo,
 maximo, media e qtd_pares. Por exemplo, para [4, 7, 1, 10] o resultado seria:"""

def estatistica(lista):
    if not lista:
        return {}
    
    resultado = {}
    resultado["maximo"] = max(lista)
    resultado["minimo"] = min(lista)
    resultado["media"] = sum(lista)/ len(lista)
    resultado["pares"] = 0

    for numero in lista:
        if numero % 2 == 0:
            resultado["pares"] +=1

    return resultado
print(estatistica([8, 9, 14, 17, 25, 98]))
    
    
             
