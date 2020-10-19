# Definimos la variable pesos para que reciba un dato.
pesos = input("¿Cuantos pesos colombianos tienes?:\n")
# Convertimos ese dato a un número de tipo flotante.
pesos = float(pesos)
# Asiganmos el valor del dolar
valor_dolar = 3875
# Hacemos el cálculo de cuantos dolares tenemos
dolares = pesos / valor_dolar
# Seleccionamos la cantidad de decimales que queremos que tenga.
dolares = round(dolares, 2)
# Convertimos el número a un string
dolares = str(dolares)
# Imprimimos el resultado.
print("Tienes $" + dolares + " dólares")