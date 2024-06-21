class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return (self.lat == other.lat) & (self.lon == other.lon)

    def __lt__(self, other): # Less Than
        return (self.lat + self.lon) < (other.lat + self.lon)

    def __le__(self, other): # Less Than
        return (self.lat + self.lon) <= (other.lat + self.lon)


coords = Coordenadas(1, 2)
coords2 = Coordenadas(1, 2)

print(coords == coords2) # False (Sin usar __eq__), True with __eq__
print(coords < coords2) # False (Is equals)
print(coords <= coords2) # True (Is equals)

