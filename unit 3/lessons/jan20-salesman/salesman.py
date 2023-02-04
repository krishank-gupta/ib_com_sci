import random
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"[Coordinate class]: x={self.x} y={self.y}"

class City:
    def __init__(self, name:str, location:Coordinate):
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return f"[City class] {self.name} located at {self.location}"

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_distance(self, other_city):
        if not isinstance(other_city, City):
            raise ValueError("City must be a city object")
        else:
            distance = (((other_city.location.x - self.location.x) ** 2) + ((other_city.location.y - self.location.y) ** 2)) ** 0.5
            return distance

class Country:
    def __init__(self, name) -> None:
        self.city_list = []
        self.name = name

    def __repr__(self) -> str:
        return f"[Country Class] {self.name} with cities: {self.city_list}"

    def add_city(self, city_to_add:City):
        if isinstance(city_to_add, City):
            self.city_list.append(city_to_add)
        else:
            raise ValueError("City must be a City Object")

    def remove_city(self, city_to_remove:City):
        self.city_list = [value for value in self.students if value != city_to_remove]

    def get_cities(self):
        return self.city_list

Japan = Country(name="Japan")

for i in range(0,10,1):
    city_names = ["Tokyo", "Okinawa", "Karuizawa", "Nagano", "Osaka", "Hiroshima", "Nagasaki", "Kyoto", "Sendai", "Chiba"]

    new_coordinate = Coordinate( random.randint(0,100), random.randint(0,100) )
    new_city = City(city_names[i], new_coordinate)

    Japan.add_city(city_to_add=new_city)

# print(Japan)

# for item in Japan.city_list:
#     min = 100
#     closestCity = []
#     for another_item in Japan.city_list:
#         if item != another_item:
#             if (item.get_distance(another_item) < min):
#                 min = item.get_distance(another_item)
#                 closestCity = another_item
    
#     print(f"{item}. Closest City: {closestCity}. Distance: {int(min)}")

x_list = []
y_list = []
names = []
for city in Japan.city_list:
    x_list.append(city.location.x)
    y_list.append(city.location.y)
    names.append(city.name)

for i in range(0, len(Japan.city_list)-1, 1):
    start_city = Japan.city_list[i]
    print()
    end_city = Japan.city_list[i+1]
    x_line = [start_city.location.x, end_city.location.x]
    y_line = [start_city.location.y, end_city.location.y]
    plt.plot(x_line, y_line, color="pink")


plt.scatter(x_list, y_list)

for i, txt in enumerate(names):
    plt.text(x_list[i]+.05, y_list[i]+.05, txt, fontsize=9)

plt.show()