from database import Database
from helpers import input_positive_int

class RentalService:
    def __init__(self):
        self.db = Database()

    def show_available_cars(self):
        print("\n--- Available Cars ---")
        for car in self.db.cars:
            if not car['rented']:
                print(f"{car['id']} - {car['brand']} {car['model']}")

    def rent_car(self):
        self.show_available_cars()
        car_id = input_positive_int("Enter Car ID to rent: ")

        for car in self.db.cars:
            if car['id'] == car_id and not car['rented']:
                customer_name = input("Enter your name: ")
                car['rented'] = True
                self.db.rentals.append({
                    "customer": customer_name,
                    "car_id": car_id
                })
                print("Car rented successfully!")
                return

        print("Car not available or invalid ID.")

    def return_car(self):
        customer_name = input("Enter your name: ")

        rental_found = None
        for rental in self.db.rentals:
            if rental['customer'] == customer_name:
                rental_found = rental
                break

        if rental_found:
            for car in self.db.cars:
                if car['id'] == rental_found['car_id']:
                    car['rented'] = False
            self.db.rentals.remove(rental_found)
            print("Car returned successfully!")
        else:
            print("No rental found for this customer.")
