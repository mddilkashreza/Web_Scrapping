import requests

PRODUCT_URL = "https://dummyjson.com/products"


# GET , POST, PUT, PATCH, DELETE


response = requests.get(PRODUCT_URL)
result = response.json()
products = result.get("products")
f = open("data.txt", "w")
# print(products)

for product in products:
    f.write(f"Title: {product.get('title')}\n")
    f.write(f"Price: {product.get('price')}\n")
    f.write(f"Brand: {product.get('brand')}\n")
    f.write("\n\n")
    # print(f"Title: {product.get('title')}")
    # print(f"Price: {product.get('price')}")
    # print("*"*50)


f.close()