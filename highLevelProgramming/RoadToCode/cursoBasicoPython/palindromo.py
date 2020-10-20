# def es_palindromo(palabra):
#     palabra = palabra.upper()
#     palabra = palabra.strip()
#     print("palabra = upper: " + palabra )
#     if palabra == palabra[::-1]:
#         print("Es palindromo")
#     else:
#         print("NO es palindromo")

# palabra = input("Escribe una palabra: ")
# print("Paso la palabra: "+ palabra)
# es_palindromo(palabra)


def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()