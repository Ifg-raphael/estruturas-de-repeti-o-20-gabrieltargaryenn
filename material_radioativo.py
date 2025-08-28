# Sua solução aqui

massa = float(input())

tempo = 0  

while massa >= 0.5:
    massa /= 2
    tempo += 50

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print(f"{int(horas)}h {int(minutos)}m {int(segundos)}s")
