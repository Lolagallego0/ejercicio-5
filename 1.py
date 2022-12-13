import time
import os
import datetime

#%d - Día del mes
#%H - Hora (formato 24 horas)
#%m - Mes en número
#%M- Minutos
#%S - Segundos
#%Y - Numero de año entero (2014)

ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
print(ahora.strftime("%d/%m/%Y, %H:%M:%S"))