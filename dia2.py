numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar de {numero}:")

contador = 1
while contador < 11:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador = contador + 1