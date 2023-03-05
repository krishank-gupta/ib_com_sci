class Bicycle:
    def __init__(self, material) -> None:
        self.wheel = Wheel(26,100,10)
        self.material = material 

    def ride(self):
        print(self.wheel.get_size(), self.material)

class Wheel(Bicycle):
    def __init__(self, size, perimeter, km_per_rotation) -> None:
        super().__init__()
        self.size = size
        self.perimeter = perimeter
        self.km_per_rotation = km_per_rotation

    def get_size(self):
        return self.size
    
    def get_perimeter(self):
        return self.perimeter
    
    def get_km_per_rotation(self):
        return self.km_per_rotation