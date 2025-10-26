from product import Product
from store import Store

print('> Создаем магазин')
store = Store()

print('> Создаем товары')
product1 = Product("Ноутбук", 1000, 5)
product2 = Product("Смартфон", 500, 10)

print('> Добавляем товары в магазин')
store.add_product(product1)
store.add_product(product2)

print('> Список всех товаров')
store.list_products()

print('> Создаем заказ')
order = store.create_order()

print('> Добавляем товары в заказ')
order.add_product(product1, 2)
order.add_product(product2, 3)

print('> Выводим общую стоимость заказа')
total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

print('> Проверяем остатки на складе после заказа')
store.list_products()

print('> Возвращем 2 ноутбука')
order.return_product(product1, 2)
print('> Проверяем остатки на складе после заказа')
store.list_products()
