n = int(input("Ingrese la cantidad de números (N < 12): "))

if n > 12:
    print("VALOR EXCEDIDO")
elif n <= 0:
    print("CANTIDAD INVALIDA")
else:
    positivos = []
    negativos = []
    ceros = 0

    for i in range(n):
        num = float(input(f"Ingrese número {i+1}: "))
        if num > 0:
            positivos.append(num)
        elif num < 0:
            negativos.append(num)
        else:
            ceros += 1

    prom_pos = sum(positivos) / len(positivos) if positivos else 0
    prom_neg = sum(negativos) / len(negativos) if negativos else 0

    print(f"Promedio de positivos: {prom_pos}")
    print(f"Promedio de negativos: {prom_neg}")
    print(f"Cantidad de ceros: {ceros}")