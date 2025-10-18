from Q1.classes.HashTable import HashTable
from Q1.classes.Product import Product
from Q1.product_data import product_data

import cli_menu
import sys


def insert_menu(hash_table: HashTable):
    print("Insert New Product")
    print(f"Product id: {Product.next_product_id()}")
    product_name = input("Product name: ")
    product_description = input("Product description: ")
    product_price = cli_menu.input_float("Product price: ")
    product_stock = cli_menu.input_int("Product stock: ")

    print("\n")
    choice = cli_menu.select(title="Confirm insertion?", choices=["Yes", "No"])
    match choice:
        case "1":
            new_product = Product(product_name, product_description, product_price, product_stock)
            hash_table.insert(new_product.id, new_product)
            input("Insertion successful.")
        case "2":
            input("Canceled insertion.")


def search_menu(hash_table: HashTable):
    product_id = input("Enter product id to search: ")
    product = hash_table.search(product_id)

    if not product:
        input("No product found.")
    else:
        input(product)


def edit_menu(hash_table: HashTable):
    product_id = input("Enter product id to edit: ")
    product = hash_table.search(product_id)

    if not product:
        input("No product found.")
        return

    while True:
        print(product)
        choice = cli_menu.select(
            title="Select property to edit: ",
            choices=["Name", "Description", "Price", "Stock", "Save changes"],
            clear_screen_after=False,
        )
        match choice:
            case "1":
                product.name = input("Enter new name: ")
            case "2":
                product.description = input("Enter new description: ")
            case "3":
                product.price = cli_menu.input_float("Enter new price: ")
            case "4":
                product.stock = cli_menu.input_int("Enter new stock: ")
            case "5":
                break
        cli_menu.clear_screen()


def delete_menu(hash_table: HashTable):
    product_id = input("Enter product id to delete: ")
    product = hash_table.search(product_id)

    if not product:
        input("No product found.")
        return

    cli_menu.clear_screen()
    print(product)

    choice = cli_menu.select(title="Confirm deletion?", choices=["Yes", "No"])
    match choice:
        case "1":
            hash_table.delete(product.id)
            input("Deletion successful.")
        case "2":
            input("Canceled deletion.")


def main():
    hash_table = HashTable(11)

    # insert pre-defined records
    for product in product_data:
        hash_table.insert(product.id, product)

    while True:
        choice = cli_menu.select(
            title="Baby Shop Inventory System",
            choices=["Insert", "Search", "Edit", "Delete", "Display hash table", "Exit program"],
        )
        match choice:
            case "1":
                insert_menu(hash_table)
            case "2":
                search_menu(hash_table)
            case "3":
                edit_menu(hash_table)
            case "4":
                delete_menu(hash_table)
            case "5":
                hash_table.print()
                input()
            case "6":
                sys.exit()

        cli_menu.clear_screen()


if __name__ == "__main__":
    main()
