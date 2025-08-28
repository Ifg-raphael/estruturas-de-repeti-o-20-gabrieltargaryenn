# Sua solução aqui

massa = float(input())

tempo_total = 0  # tempo em segundos

while massa >= 0.5:
    massa /= 2
    tempo_total += 50

horas = tempo_total // 3600
minutos = (tempo_total % 3600) // 60
segundos = tempo_total % 60

print(f"{int(horas)}h {int(minutos)}m {int(segundos)}s")