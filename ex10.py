from datetime import timedelta

sec = int(input("Digite a duração em segundos: "))
horas = timedelta(seconds=sec)

print(horas)