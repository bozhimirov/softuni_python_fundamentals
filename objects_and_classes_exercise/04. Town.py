class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = 0
        self.longitude = 0

    def set_latitude(self, value):
        self.latitude = value

    def set_longitude(self, new_value):
        self.longitude = new_value

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
