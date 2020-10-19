# Definimos la variable pesos para que reciba un dato.
dolares = input("¿Cuantos dolares tienes?: ")
# Convertimos ese dato a un número de tipo flotante.
dolares = float(dolares)
# Asiganmos el valor del dolar
valor_peso_colombiano = 3875
# Hacemos el cálculo de cuantos dolares tenemos
pesos = dolares * valor_peso_colombiano
# Seleccionamos la cantidad de decimales que queremos que tenga.
pesos = round(pesos, 2)
# Convertimos el número a un string
pesos = str(pesos)
# Imprimimos el resultado.
print("Tienes $" + pesos + " pesos colombianos.")