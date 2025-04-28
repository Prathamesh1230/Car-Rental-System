from rental_service import RentalService
from helpers import input_positive_int

class RentalController:
    def __init__(self):
        self.rental_service = RentalService()

    def customer_menu(self):
        while True:
            print("\n--- Customer Menu ---")
            print("1. View Available Cars")
            print("2. Rent a Car")
            print("3. Return a Car")
            print("4. Back")

            choice = input("Enter choice: ")

            if choice == '1':
                self.rental_service.show_available_cars()
            elif choice == '2':
                self.rental_service.rent_car()
            elif choice == '3':
                self.rental_service.return_car()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")
