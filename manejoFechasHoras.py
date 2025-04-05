#!/usr/bin/env python3

import datetime

ahora = datetime.datetime.now()
print(ahora)

año = ahora.year
mes = ahora.month
dia = ahora.day
horas = ahora.hour
minutos = ahora.minute
segundos = ahora.second

print(f"\nAño: {año}, mes: {mes}, dia: {dia}, {horas}:{minutos}:{segundos}")