from random import randint

N = 1000
total_numeros = 100

with open("largefile", "w", encoding="utf-8") as f:
    for _ in range(total_numeros):
        n = randint(0, N)
        f.write(f"{n}\n")

print(f"Archivo 'largefile' creado con {total_numeros} elementos! :)")