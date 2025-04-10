product_name = input("Cual es nombre del producto?: ")
product_category = input("Cual es la categoria del productos? (ropa, electronicos, alimentos): ")
base_price = float(input("Cual es el precio inicial del producto?: "))

if product_category == "ropa":
    new_price = base_price * 1.30
elif product_category == "electronicos":
    new_price = base_price * 1.20
elif product_category == "alimentos":
    new_price = base_price * 1.10
else:
    print("Categoria no valida")
    exit()

print("El producto esta a la venta")

buyed_product = input("El producto fue comprado? (si/no): ")

while buyed_product == "no" and new_price > base_price:
    new_price = new_price * (1 - 0.03)
    buyed_product = input("El producto fue comprado? (si/no): ")

if new_price < base_price:
    new_price = base_price

print(
    f"El producto {product_name} con precio inicial {base_price} "
    f"termino con un precio de {new_price}."
)
