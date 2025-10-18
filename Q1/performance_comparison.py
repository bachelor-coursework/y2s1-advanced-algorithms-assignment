from Q1.classes.HashTable import HashTable
from Q1.classes.Product import Product
from Q1.product_data import product_data

import time


def hash_table_performance(hash_table: HashTable):
    total_time_taken = 0
    number_of_products = 0

    for product in product_data:
        start = time.perf_counter()
        hash_table.search(product.id)
        end = time.perf_counter()

        total_time_taken += end - start
        number_of_products += 1
    return total_time_taken / number_of_products


def one_dimensional_array_performance(array: list[Product]):
    total_time_taken = 0
    number_of_products = 0

    for product in product_data:
        start = time.perf_counter()
        for entry in array:
            if entry.id == product.id:
                break
        end = time.perf_counter()

        total_time_taken += end - start
        number_of_products += 1
    return total_time_taken / number_of_products


def main():
    hash_table = HashTable(10)
    array = []

    for product in product_data:
        hash_table.insert(product.id, product)
        array.append(product)

    hash_table_average_time = hash_table_performance(hash_table)
    array_average_time = one_dimensional_array_performance(array)
    print(
        f"""
Performance between
Hash Table: {hash_table_average_time * 1_000_000:.2f}µs
One Dimensional Array: {array_average_time * 1_000_000:.2f}µs

Difference: {abs(hash_table_average_time - array_average_time) * 1_000_000:.2f}µs
"""
    )


if __name__ == "__main__":
    main()
