import datetime

from typing import Dict
from product import Product

class Order:
    """Заказ покупателя"""
    def __init__(self):
        self._products: Dict[Product, int] = {}
        self._created_at = datetime.datetime.now()

    def add_product(self, product: Product, quantity: int) -> None:
        """Добавляет товар в заказ. Проверяет наличие на складе."""

        if product.stock < quantity:
            raise ValueError(f"Ошибка: недостаточно товара '{product.name}' на складе. Доступно: {product.stock}, требуется: {quantity}")
        
        if product in self._products:
            self._products[product] += quantity
        else:
            self._products[product] = quantity

        product.update_stock(-quantity)

    def remove_product(self, product: Product, quantity: int) -> None:
        """Удаляет указанное количество товара из заказа. Не актуализирует товар на складе!"""
        self.check_product(product)

        if self._products[product] < quantity:
            del self._products[product]
        else:
            self._products[product] -= quantity

    def return_product(self, product, quantity) -> None:
        """Возвращает товар в магазин (увеличивает запас на складе)."""
        self.check_product(product)

        removed_quantity = min(quantity, self._products[product])
        self.remove_product(product, removed_quantity)
        product.update_stock(removed_quantity)

    def calculate_total(self) -> float:
        """Рассчитывает общую стоимость заказа."""
        total = 0.0
        for product, quantity  in self._products.items():
            total += product.price * quantity
        return total
    
    def check_product(self, product) -> None:
        """Проверяет товар в заказе"""
        if product not in self._products:
            raise KeyError(f"Товар {product.name} не найден в заказе")
