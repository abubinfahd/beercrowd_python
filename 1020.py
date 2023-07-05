days = int(input())

years = int(days/365)
days -= years*365

months = int(days/30)
days -= months*30

print("{} ano(s)".format(int(years)))
print("{} mes(es)".format(int(months)))
print("{} dia(s)".format(int(days)))