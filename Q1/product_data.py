from Q1.classes.Product import Product

product_data = [
    Product("Baby Diapers", "Soft and breathable diapers for day and night use", 45.90, 120),
    Product("Baby Wipes", "Fragrance-free gentle wipes for baby’s sensitive skin", 15.50, 300),
    Product("Baby Lotion", "Moisturizing baby lotion with natural ingredients", 22.00, 180),
    Product("Baby Shampoo", "Tear-free mild shampoo for daily cleansing", 19.90, 150),
    Product("Baby Powder", "Hypoallergenic powder to keep baby dry and fresh", 14.50, 200),
    Product("Baby Bottle 250ml", "BPA-free feeding bottle with anti-colic nipple", 25.00, 90),
    Product("Pacifier Set", "Set of 2 orthodontic silicone pacifiers", 18.90, 140),
    Product("Baby Blanket", "Soft cotton blanket suitable for newborns", 35.00, 80),
    Product("Baby Bibs", "Waterproof bibs for mess-free feeding time", 16.50, 170),
    Product("Baby Oil", "Gentle baby oil to nourish skin after bath", 20.00, 130),
    Product("Baby Wash", "2-in-1 baby body wash and shampoo combo", 24.90, 110),
    Product("Baby Nail Clipper", "Safe rounded-tip nail clipper for tiny nails", 12.00, 95),
    Product("Teething Toy", "Colorful silicone teething ring for soothing gums", 17.50, 160),
    Product("Baby Onesie", "Soft cotton onesie, fits 0-6 months", 29.90, 70),
    Product("Baby Socks", "Pack of 3 soft cotton socks for babies", 13.90, 200),
    Product("Stroller", "Lightweight foldable stroller for easy travel", 299.00, 25),
    Product("Baby Carrier", "Ergonomic front and back baby carrier", 159.00, 40),
    Product("Baby Monitor", "Wireless baby monitor with night vision", 259.00, 30),
    Product("Baby Feeding Set", "Complete feeding set with plate, bowl, spoon, fork", 39.90, 90),
    Product("Baby Bath Tub", "Portable non-slip baby bath tub with support", 89.00, 45),
]

big_product_data = []
for i in range(1_000):
    big_product_data.append(Product(f"Product Name {i}", f"Description {i}", 20.0, 1))
