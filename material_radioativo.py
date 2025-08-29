# Sua solução aqui

massa_inicial = float(input())

massa = massa_inicial
tempo_segundos = 0

while massa >= 0.5:
    massa /= 2
    tempo_segundos += 50

horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60

print(f"{int(horas)}h {int(minutos)}m {int(segundos)}s")
