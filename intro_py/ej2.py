catalogo = int(input("Ingrese número de catálogo: "))

if catalogo < 1200 or catalogo > 90000:
    print("FUERA DE CATALOGO")
else:
    es_defectuoso = (12121 <= catalogo <= 18081) or \
                    (30012 <= catalogo <= 45565) or \
                    (67000 <= catalogo <= 68000)
    
    if es_defectuoso:
        print("FUERA DE CATALOGO")
    else:
        print("Artículo OK")