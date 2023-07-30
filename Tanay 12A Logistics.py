# Logistics Management
"""
Fields :- ['ProductID', 'ProductName', 'Quantity', 'Cost', 'CustomerPhoneNo.']
1. Add New product
2. View products
3. Search product
4. Update product
5. Delete product
6. Quit
"""
print('''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              
                                                              
''')
import csv
# Define global variables
product_fields = ['ProductID', 'ProductName', 'Quantity', 'Cost', 'CustomerPhoneNo.']
product_database = 'products.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Logistics Management")
    print("---------------------------------------")
    print("1. Add New product")
    print("2. View products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Quit")


def add_product():
    print("-------------------------")
    print("Add product Information")
    print("-------------------------")
    global product_fields
    global product_database

    product_data = []
    for field in product_fields:
        value = input("Enter " + field + ": ")
        product_data.append(value)

    with open(product_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([product_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_products():
    global product_fields
    global product_database

    print("--- product Records ---")

    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in product_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_product():
    global product_fields
    global product_database

    print("--- Search product ---")
    ProductID = input("Enter ProductID no. to search: ")
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ProductID == row[0]:
                    print("----- product Found -----")
                    print("ProductID: ", row[0])
                    print("ProductName: ", row[1])
                    print("Quantity: ", row[2])
                    print("Cost: ", row[3])
                    print("CustomerPhoneNo.: ", row[4])
                    break
        else:
            print("ProductID No. not found in our database")
    input("Press any key to continue")


def update_product():
    global product_fields
    global product_database

    print("--- Update product ---")
    ProductID = input("Enter ProductID no. to update: ")
    index_product = None
    updated_data = []
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ProductID == row[0]:
                    index_product = counter
                    print("product Found: at index ",index_product)
                    product_data = []
                    for field in product_fields:
                        value = input("Enter " + field + ": ")
                        product_data.append(value)
                    updated_data.append(product_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_product is not None:
        with open(product_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ProductID No. not found in our database")

    input("Press any key to continue")


def delete_product():
    global product_fields
    global product_database

    print("--- Delete product ---")
    ProductID = input("Enter ProductID no. to delete: ")
    product_found = False
    updated_data = []
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ProductID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    product_found = True

    if product_found is True:
        with open(product_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ProductID no. ", ProductID, "deleted successfully")
    else:
        print("ProductID No. not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        search_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    else:
        break

print("-------------------------------")
print(" Thank you ")
print("-------------------------------")
