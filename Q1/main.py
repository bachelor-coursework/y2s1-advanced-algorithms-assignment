from Q1.classes.HashTable import HashTable
from Q1.classes.Product import Product

import cli_menu
import sys


def insert_menu():
    choice = cli_menu.select(title="Insert New Product", choices=["Insert", "Search", "Edit", "Delete"])


def main():
    hash_table = HashTable(11)

    # pre-defined records
    products = [
        Product("BP001", "Baby Diapers (Small)", "Soft, leak-proof diapers for newborns.", 28.90, 120),
        Product("BP002", "Baby Lotion (200ml)", "Gentle moisturizing lotion for baby skin.", 15.50, 80),
        Product("BP003", "Feeding Bottle (250ml)", "BPA-free feeding bottle with anti-colic design.", 22.00, 60),
    ]
    for product in products:
        hash_table.insert(product.id, product)

    while True:
        choice = cli_menu.select(title="Baby Shop Inventory System", choices=["Insert", "Search", "Edit", "Delete"])
        match choice:
            case "1":
                pass
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
