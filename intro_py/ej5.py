primos = []
for num in range(2, 101):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print(f"Números primos encontrados: {primos}")
print(f"Total de primos: {len(primos)}")