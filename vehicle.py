class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rent_per_day = rent_per_day
        self.is_available = True
