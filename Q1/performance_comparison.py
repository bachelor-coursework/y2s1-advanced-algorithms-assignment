from Q1.classes.HashTable import HashTable
from Q1.classes.Product import Product
from Q1.product_data import product_data, big_product_data

import cli_menu
import time
import random


def hash_table_performance(hash_table: HashTable, data: list[Product]):
    total_time_taken = 0
    number_of_products = len(data)

    for product in data:
        start = time.perf_counter()
        hash_table.search(product.id)
        end = time.perf_counter()

        total_time_taken += end - start

    return total_time_taken / number_of_products


def one_dimensional_array_performance(array: list[Product], data: list[Product]):
    total_time_taken = 0
    number_of_products = len(data)

    for product in data:
        start = time.perf_counter()
        for entry in array:
            if entry.id == product.id:
                break
        end = time.perf_counter()

        total_time_taken += end - start

    return total_time_taken / number_of_products


def main():
    choice = cli_menu.select("Select test data size", choices=["small", "large"])
    match (choice):
        case "1":
            hash_table = HashTable(10)
            test_data = product_data
        case "2":
            hash_table = HashTable(1000)
            test_data = big_product_data

    for product in test_data:
        hash_table.insert(product.id, product)

    array = test_data.copy()
    random.shuffle(test_data)

    hash_table_average_time = hash_table_performance(hash_table, test_data)
    array_average_time = one_dimensional_array_performance(array, test_data)
    print(
        f"""
Average time taken per product search
Hash Table: {hash_table_average_time * 1_000_000:.2f}µs
One Dimensional Array: {array_average_time * 1_000_000:.2f}µs

Difference: {abs(hash_table_average_time - array_average_time) * 1_000_000:.2f}µs
"""
    )


if __name__ == "__main__":
    main()
