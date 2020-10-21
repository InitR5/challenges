from math import sqrt


def es_primo(numero):
    # contador = 0 

    # for i in range (1, numero + 1):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False
    
    if numero % 2 != 0 or numero == 2:
        contador = 0
        numero = round(sqrt(numero))
        for i in range (1, numero + 1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                contador += 1
        print(contador)
        if contador == 0:
            return True 

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()