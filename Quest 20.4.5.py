import json
from collections import defaultdict

# Загрузка данных
with open("orders_july_2023.json", "r") as file:
    orders = json.load(file)

# Фильтрация заказов за июль 2023 (даты вида "2023-XX-07", где XX от 01 до 31)
july_orders = {
    order_num: order_data
    for order_num, order_data in orders.items()
    if order_data['date'].endswith('-07') and
       1 <= int(order_data['date'].split('-')[1]) <= 31
}

# 1. Самый дорогой заказ
max_price_order = max(july_orders.items(), key=lambda x: x[1]['price'])[0]

# 2. Заказ с наибольшим количеством товаров
max_quantity_order = max(july_orders.items(), key=lambda x: x[1]['quantity'])[0]

# 3. День с наибольшим количеством заказов
date_counts = defaultdict(int)
for order_data in july_orders.values():
    date_counts[order_data['date']] += 1
most_orders_date = max(date_counts.items(), key=lambda x: x[1])[0]

# 4. Пользователь с наибольшим количеством заказов
user_order_counts = defaultdict(int)
for order_data in july_orders.values():
    user_order_counts[order_data['user_id']] += 1
most_orders_user = max(user_order_counts.items(), key=lambda x: x[1])[0]

# 5. Пользователь с наибольшей суммарной стоимостью заказов
user_total_spent = defaultdict(int)
for order_data in july_orders.values():
    user_total_spent[order_data['user_id']] += order_data['price']
top_spender = max(user_total_spent.items(), key=lambda x: x[1])[0]

# 6. Средняя стоимость заказа
average_order_price = sum(
    order['price'] for order in july_orders.values()
) / len(july_orders)

# 7. Средняя стоимость товара
average_item_price = sum(
    order['price'] for order in july_orders.values()
) / sum(
    order['quantity'] for order in july_orders.values()
)

# Вывод результатов
print("Анализ за июль 2023 года:")
print("----------------------------------------")
print(f"1. Самый дорогой заказ: {max_price_order} (цена: {july_orders[max_price_order]['price']})")
print(f"2. Заказ с наибольшим количеством товаров: {max_quantity_order} ({july_orders[max_quantity_order]['quantity']} шт.)")
print(f"3. День с наибольшим количеством заказов: {most_orders_date} ({date_counts[most_orders_date]} заказов)")
print(f"4. Пользователь с наибольшим количеством заказов: {most_orders_user} ({user_order_counts[most_orders_user]} заказов)")
print(f"5. Пользователь с наибольшей суммарной стоимостью заказов: {top_spender} (потратил: {user_total_spent[top_spender]})")
print(f"6. Средняя стоимость заказа: {average_order_price:.2f}")
print(f"7. Средняя стоимость товара: {average_item_price:.2f}")