a = int(input("Valor A (divisor): "))
b = int(input("Valor B (límite superior): "))

sumatoria = 0
cantidad_total = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    
    cantidad_total += 1
    if num % a == 0 and num < b:
        sumatoria += num

print(f"Sumatoria resultante: {sumatoria}")
print(f"Cantidad total de números ingresados: {cantidad_total}")