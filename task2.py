import requests
import pytest

API_URL = "https://fakestoreapi.com/products"

def fetch_products():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    return response.json()

def is_product_defective(product):
    title = product.get("title", "")
    price = product.get("price", 0)
    rating = product.get("rating", {})

    # Проверка: название не должно быть пустым
    if not title.strip():
        return True

    # Проверка: цена не должна быть отрицательной
    if isinstance(price, (int, float)) and price < 0:
        return True

    # Проверка: рейтинг (если есть) не должен превышать 5
    rate = rating.get("rate")
    if isinstance(rate, (int, float)) and rate > 5:
        return True

    return False

def test_product_data_validation():
    products = fetch_products()
    defective_products = [product for product in products if is_product_defective(product)]

    if defective_products:
        print(f"❌ Найдены продукты с дефектами: {len(defective_products)}")
        for product in defective_products:
            print(product)
    else:
        print("✅ Все продукты корректны.")

    assert not defective_products, "Обнаружены продукты с некорректными данными"
