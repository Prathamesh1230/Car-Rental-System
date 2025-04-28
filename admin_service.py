from database import Database
from helpers import input_positive_int

class AdminService:
    def __init__(self):
        self.db = Database()

    def add_car(self):
        brand = input("Enter car brand: ")
        model = input("Enter car model: ")
        new_car = {
            "id": self.db.get_next_car_id(),
            "brand": brand,
            "model": model,
            "rented": False
        }
        self.db.cars.append(new_car)
        print("Car added successfully!")

    def remove_car(self):
        self.view_all_cars()
        car_id = input_positive_int("Enter Car ID to remove: ")

        for car in self.db.cars:
            if car['id'] == car_id:
                self.db.cars.remove(car)
                print("Car removed successfully!")
                return
        print("Car ID not found.")

    def view_all_cars(self):
        print("\n--- All Cars ---")
        for car in self.db.cars:
            status = "Rented" if car['rented'] else "Available"
            print(f"{car['id']} - {car['brand']} {car['model']} ({status})")

    def view_rentals(self):
        print("\n--- Current Rentals ---")
        for rental in self.db.rentals:
            print(f"Customer: {rental['customer']}, Car ID: {rental['car_id']}")
