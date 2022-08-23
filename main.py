import customer_operations.user
from customer_operations.admin import Admin

# import customer operations
print("......Bank Customer Portal......")


def main():
    print("Enter")
    print("\t1. Admin Login")
    print("\t2. User Login")
    print("\t3. Exit\n")

    operation_select = int(input())

    if operation_select == 1:
        Admin.admin_login(Admin)

    if operation_select == 2:
        customer_operations.user

    if operation_select == 3:
        pass


main()
