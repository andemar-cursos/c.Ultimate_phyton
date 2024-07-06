from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1)
# fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)
print("dias", delta.days) # dias 31
print("segundos", delta.seconds) # segundos 0
print("microsegundos", delta.microseconds) # microsegundos 0
print("total_seconds()", delta.total_seconds()) # total_seconds() 2678400.0

