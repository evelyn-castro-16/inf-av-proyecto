for i in range(100):
    print(f"\nIntento {i+1}")
    a = float(input("Ingrese A: "))
    b = float(input("Ingrese B: "))
    c = float(input("Ingrese C: "))

    if a == 0 and b == 0 and c == 0:
        print("Terna nula. Programa finalizado.")
        break
    
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        print("La ecuación tiene raíces COMPLEJAS.")
    else:
        print("La ecuación tiene raíces reales.")