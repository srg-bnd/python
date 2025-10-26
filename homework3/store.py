
import datetime

from typing import List
from order import Order
from product import Product

class Store:
    """Магазин, управляющий товарами и заказами"""
    def __init__(self):
        self._products: List[Product] = []
        self._orders: List[Order] = []
        self._created_at = datetime.datetime.now()

    @property
    def products(self) -> List[Product]:
        """Список всех доступных товаров в магазине."""
        return self._products

    def add_product(self, product: Product) -> None:
        """Добавляет товар в магазин."""
        if product in self._products:
            raise ValueError(f'!Товар {product.name} уже существует')
        self._products.append(product)

    def list_products(self) -> None:
        """Отображает все товары в магазине."""
        if not self.products:
            print("В магазине нет товаров.")
            return

        for product in self._products:
            print(f"- {product.name}: {product.price} у.e., на складе: {product.stock} шт.")

    def create_order(self) -> Order:
        """Создание нового заказа"""
        order = Order()
        self._orders.append(order)

        return order
