# Ejemplo calcular medias de tres valores
def calcular_media(*args):
    total = 0
    for i in args:
        total += i
    resultado_media = total / len(args)
    return resultado_media

a, b, c = 5, 42, 23
media = calcular_media(a, b, c)
# F string para calcular media
print(f'La media de {a}, {b} y {c} es {media}')