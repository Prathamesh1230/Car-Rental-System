from admin_service import AdminService

class AdminController:
    def __init__(self):
        self.admin_service = AdminService()

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Car")
            print("2. Remove Car")
            print("3. View All Cars")
            print("4. View Rentals")
            print("5. Back")

            choice = input("Enter choice: ")

            if choice == '1':
                self.admin_service.add_car()
            elif choice == '2':
                self.admin_service.remove_car()
            elif choice == '3':
                self.admin_service.view_all_cars()
            elif choice == '4':
                self.admin_service.view_rentals()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")
