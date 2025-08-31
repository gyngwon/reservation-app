class Show:
    def __init__(self, name, capacity=100):
        self.id = None
        self.name = name
        self.capacity = capacity
        self.available_seats = capacity

class Booking:
    def __init__(self, show_id):
        self.id = None
        self.show_id = show_id
