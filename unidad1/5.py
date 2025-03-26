entrada = input("Entero:")
while len(entrada)!= 5 :
    print(f"Entrada: {len(entrada)}")
    print("Debe ser un entero de 5 digitos...")
    entero = int(input("Entero:"))
print(f"{pow(int(entrada[0:1]),2)} {pow(int(entrada[1:2]),2)} {pow(int(entrada[2:3]),2)} {pow(int(entrada[3:4]),2)} {pow(int(entrada[4:5]),2)}")