from rental_controller import RentalController
from admin_controller import AdminController

def main():
    print("Welcome to Car Rental System")
    rental_controller = RentalController()
    admin_controller = AdminController()

    while True:
        print("\n1. Customer Portal")
        print("2. Admin Portal")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            rental_controller.customer_menu()
        elif choice == '2':
            admin_controller.admin_menu()
        elif choice == '3':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
