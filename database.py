class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.cars = [
            {"id": 1, "brand": "Toyota", "model": "Corolla", "rented": False},
            {"id": 2, "brand": "Honda", "model": "Civic", "rented": False},
            {"id": 3, "brand": "Ford", "model": "Focus", "rented": False},
        ]
        self.rentals = []

    def get_next_car_id(self):
        if self.cars:
            return max(car['id'] for car in self.cars) + 1
        else:
            return 1
