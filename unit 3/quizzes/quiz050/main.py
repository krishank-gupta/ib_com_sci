class flight:
    def __init__(self, flight_number, origin, destination, departure_time, duration) -> None:
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration

    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes and {self.duration[2]} seconds"
    

flight1 = flight("AA123", "New York", "Los Angeles", "10:00 AM", [5,30,3])
flight2 = flight("JY134", "Tokyo Narita", "Okinawa", "04:00 PM", [1,22,3])

print(flight1.get_duration())
print(flight2.get_duration())


    