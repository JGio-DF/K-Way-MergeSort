from random import randint

# Este programa crea un archivo llamado "largefile" con 100 números aleatorios, el programa principal divide esos 100 números en bloques de 10 : )

N = 1000
f = open("largefile", "w")
k = 0

while True:
    n = randint(0, N)
    f.write(str(n) + "\n")
    k = k + 1
    if k == 100:
        f.close()
        break

print("Archivo creado! :)")
