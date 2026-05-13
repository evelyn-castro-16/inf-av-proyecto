n = int(input("Ingrese un número para calcular su factorial: "))
if n < 0:
    print("No existe factorial de números negativos.")
else:
    resultado = 1
    aux = n
    while aux > 1:
        resultado *= aux
        aux -= 1
    print(f"El factorial de {n} es: {resultado}")