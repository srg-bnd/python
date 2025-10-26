import datetime

class Product:
    """Товар в магазине"""
    def __init__(self, name: str, price: float, stock: int):
        self._name = name
        self._price = price
        self._stock = stock
        self._created_at = datetime.datetime.now()

    @property
    def name(self) -> str:
        """Название товара"""
        return self._name

    @property
    def price(self) -> float:
        """Цена товара"""
        return self._price

    @property
    def stock(self) -> int:
        """Количество товара на складе"""
        return self._stock


    def update_stock(self, quantity: int) -> None:
        """Обновляет количество товара на складе. При отрицательном значении выдаёт ошибку."""
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError(f"Ошибка: недостаточно товара '{self.name}' на складе. Текущий остаток: {self.stock}")
        self._stock = new_stock
