"""
Segunda Pregunta – ¿Cuántos Domingos?.

ref: https://docs.python.org/3.7/library/datetime.html
"""

from datetime import date, timedelta

def todos_los_domingos(year, year2):
    total = 0
    dt = date(year, 1, 1)
    dt_finish = date(year2, 12, 31)
    print("Inicio {}, Final {}".format(dt.strftime("%Y-%m-%d"), dt_finish.strftime("%Y-%m-%d")))
    dt += timedelta(days = 6 - dt.weekday())
    while dt.year <= year2:
        if ( dt.day == 1 ):
            # print("{}".format(dt.strftime("%A")))
            total += 1
        dt += timedelta(days = 7)
    return total

print(todos_los_domingos(1901, 2002))

