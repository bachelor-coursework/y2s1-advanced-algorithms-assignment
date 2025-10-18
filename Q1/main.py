from Q1.classes.HashTable import HashTable
from Q1.classes.Product import Product

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


def main():
    hash_table = HashTable(11)

    # pre-defined records
    products = [
        Product("Baby Diapers (Small)", "Soft, leak-proof diapers for newborns.", 28.90, 120),
        Product("Baby Lotion (200ml)", "Gentle moisturizing lotion for baby skin.", 15.50, 80),
        Product("Feeding Bottle (250ml)", "BPA-free feeding bottle with anti-colic design.", 22.00, 60),
    ]
    for product in products:
        hash_table.insert(product.id, product)

    while True:
        choice = cli_menu.select(title="Baby Shop Inventory System", choices=["Insert", "Search", "Edit", "Delete"])
        match choice:
            case "1":
                insert_menu(hash_table)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                sys.exit()


if __name__ == "__main__":
    main()
