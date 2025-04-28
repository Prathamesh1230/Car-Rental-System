from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rent_per_day, car_type):
        super().__init__(vehicle_id, brand, model, year, rent_per_day)
        self.car_type = car_type
