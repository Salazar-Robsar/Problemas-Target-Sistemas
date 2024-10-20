palavra = input().lower()

letra_a = 0
for a in palavra:
    if a == 'a':
        letra_a += 1
if letra_a == 0:
    print("Não há nenhuma letra 'a' nesta palavra.")
elif letra_a == 1:
    print("Existe 1 letra 'a' nesta palavra")
else:
    print(f"Existem {letra_a} letras 'a' nesta palavra")

