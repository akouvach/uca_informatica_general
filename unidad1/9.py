entrada = input("Entero:")
longitud = len(entrada)
while longitud%2 == 0 :
    print(f"Entrada: {longitud}")
    print("Debe ser una cantidad impar...")
    entrada = input("Entero:")
    longitud = len(entrada)

ini=0
medio=int(longitud/2)
fin=longitud-1
print(f"E: {entrada}, l:{longitud} - p:{entrada[ini:ini+1]}, c:{entrada[medio:medio+1]}, u:{entrada[fin:fin+1]}")
