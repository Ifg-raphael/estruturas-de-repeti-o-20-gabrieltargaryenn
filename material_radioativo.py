# Sua solução aqui

import math

massa_inicial = float(input())

# calcula número mínimo de decaimentos
n = math.ceil(math.log(massa_inicial / 0.5, 2))

# tempo total em segundos
tempo_segundos = n * 50

horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60

print(f"{int(horas)}h {int(minutos)}m {int(segundos)}s")
