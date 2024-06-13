def contarvocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador = contador + 1
    return contador

cadena = "Hola, buen dia"
resultado = contarvocales(cadena)
print(f'En esta cadena hay {resultado} vocales.')
