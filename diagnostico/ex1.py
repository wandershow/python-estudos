"""O que o programa deve fazer:

Pedir um número ao usuário.
Dizer se o número é par ou ímpar.
Mostrar a tabuada dele de 1 a 10."""

numero = int(input ("digite um numero: "))

if numero % 2 == 0:
    print(f"o numero {numero} é par")
else:
    print(f"o numero {numero} é impar")

for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
