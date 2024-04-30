class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(12, 4)
print(p.x)
print(p.y)

# class FLight()
# methods: add_passengers, open_seats
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people: 
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully!")
    else: 
        print(f"No seats are currently available for {person}.")