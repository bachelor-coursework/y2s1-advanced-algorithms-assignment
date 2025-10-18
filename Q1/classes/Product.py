class Product:
    _current_id = 1

    def __init__(self, name: str, description: str, price: float, stock: int):
        self.id = Product.next_product_id()
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

        Product._current_id += 1

    @staticmethod
    def next_product_id():
        return f"P{Product._current_id:04}"
