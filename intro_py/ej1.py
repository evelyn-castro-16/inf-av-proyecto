numero = int(input("Ingrese un número de 3 cifras: "))

if 100 <= numero <= 999:
    centena = numero // 100
    decena = (numero // 10) % 10
    unidad = numero % 10

    print(f"Centena: {centena}")
    print(f"Decena: {decena}")
    print(f"Unidad: {unidad}")
else:
    print("El número no es de 3 cifras.")