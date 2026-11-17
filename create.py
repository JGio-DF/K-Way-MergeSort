from random import randint

N = 1000
total_numeros = 100  # Cámbialo a 0 (vacío), 105 (no múltiplo), 100000 (prueba grande), etc.

with open("largefile", "w", encoding="utf-8") as f:
    for _ in range(total_numeros):
        n = randint(0, N)
        f.write(f"{n}\n")

print(f"Archivo 'largefile' creado con {total_numeros} elementos! :)")