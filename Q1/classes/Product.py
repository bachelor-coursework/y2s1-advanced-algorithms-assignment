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

    def __str__(self) -> str:
        return f"{self.id}: {self.name}, {self.description[:20] + '...' if len(self.description) > 20 else self.description} | ${self.price:.2f}, {self.stock} left."
