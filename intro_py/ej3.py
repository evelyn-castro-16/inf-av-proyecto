import math

l1 = float(input("Ingrese distancia hacia el Este (km): "))
l2 = float(input("Ingrese distancia hacia el Norte (km): "))

desplazamiento = math.sqrt(l1**2 + l2**2) # teorema de pitágoras

print(f"El desplazamiento resultante es: {desplazamiento:.2f} km")