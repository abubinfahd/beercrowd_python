days = int(input())

years = int(days/365)
days -= years*365

months = int(days/30)
days -= months*30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')