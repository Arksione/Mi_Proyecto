#1: Básico
print("Números del 0 al 100")
for numero in range(101):
    print(numero)

#2: Múltiplos de 2
print("Múltiplos de 2 del 2 hasta 500")
for numero in range(2, 501):
    if numero % 2 == 0:
        print(numero)

#3: Contando Vanilla Ice
print("Contando Vanilla Ice")
for numero in range(1, 101):
    if numero % 10 == 0:
        print("baby")
    elif numero % 5 == 0:
        print("ice ice")
    else:
        print(numero)

#4: Wow. Número gigante a la vista
print("Sumar todos los pares del 0 al 500000")
suma = 0
for numero in range(0, 500001):
    if numero % 2 == 0:
        suma += numero
print("La suma total es:", suma)

#5: Regrésame al 3
print("Contar desde 2024 hacia atrás de 3 en 3")
for numero in range(2024, 0, -3):
    print(numero)

#6: Contador dinámico
print("Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2

for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)

