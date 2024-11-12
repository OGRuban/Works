# Ось так нам допоміг ChatGPT зробити опис
class car:
    """
Клас Автомобіль представляє модель автомобіля, що має основні характеристики та функції, пов’язані з його експлуатацією. 
Він дозволяє моделювати рух автомобіля та управління його паливом.

Атрибути:
модель (str): Назва або модель автомобіля.
паливо (float): Кількість пального, доступного в автомобілі, вимірюється в літрах.
швидкість (float): Поточна швидкість автомобіля, вимірюється в км/год.
"""
"""
    Методи:
        __init__(модель, паливо): 
        Конструктор класу. Ініціалізує новий об'єкт автомобіля з вказаною моделлю та початковою кількістю пального.
        рухатися(швидкість): 
        Метод, який задає автомобілю нову швидкість і зменшує кількість пального відповідно до споживання (0.1 літра на км/год). 
        Виводить повідомлення про рух автомобіля або інформує, якщо пального недостатньо.
        заправити(кількість):
        Метод, що дозволяє додати певну кількість пального в автомобіль.
        Виводить повідомлення про успішну заправку та оновлену кількість пального.
    """