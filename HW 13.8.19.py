# Запрашиваем количество билетов
num_tickets = int(input("Введите количество билетов: "))

# Счетчик количества посетителей младше 18 лет
num_under_18 = 0

# Счетчик количества посетителей от 18 до 25 лет
num_18_to_25 = 0

# Счетчик количества посетителей старше 25 лет
num_over_25 = 0

# Запрашиваем возраст каждого посетителя и подсчитываем сумму заказа
total_price = 0
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        num_under_18 += 1
        # Билет бесплатный
        price = 0
    elif age < 25:
        num_18_to_25 += 1
        # Стоимость билета - 990 рублей
        price = 990
    else:
        num_over_25 += 1
        # Стоимость билета - 1390 рублей
        price = 1390
    total_price += price

# Проверяем, полагается ли скидка
if num_tickets > 3:
    discount = 0.1 * total_price
else:
    discount = 0

# Считаем итоговую сумму к оплате с учетом скидки
final_price = total_price - discount

# Выводим результат
print("Стоимость заказа:", total_price)
print("Скидка:", discount)
print("Итоговая стоимость к оплате:", final_price)
