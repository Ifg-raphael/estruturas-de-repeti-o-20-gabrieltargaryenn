# Sua solução aqui

massa = float(input())

n = 0
while massa >= 0.5:
    n += 1
    massa = massa / 2

tempo = n * 50

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
segundos = tempo % 60

print(f"{horas}h {minutos}m {segundos}s")
