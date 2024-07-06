
# import time
# print(time.time()) # 1720146111.7379894


from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
ahora = datetime.now()
print(fecha) # 2023-01-01 00:00:00
print(ahora) # 2024-07-04 21:23:56.162464

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")

print(fechaStr) # 2023-01-03 00:00:00
print(fecha.strftime("%Y.%m.%d")) # 2023.01.01
print(fecha > fecha2) # False

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
    fecha.second,
) # 2023 1 1 0 0 0

