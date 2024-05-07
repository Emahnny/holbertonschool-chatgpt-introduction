#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) < 2:
    print("Por favor, proporciona un número como argumento.")
    sys.exit()

numero = int(sys.argv[1])
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
