class AutoSalon:
    _instance = None  # Приватна змінна для зберігання єдиного екземпляра

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Створюємо екземпляр тільки якщо його ще не існує
            cls._instance = super(AutoSalon, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            # Ініціалізація екземпляра класу, якщо він не був ініціалізований раніше
            self.cars = []  # Приклад полегшеної ініціалізації, можна додати більше логіки

            self.initialized = True

    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars


# Приклад використання:

salon1 = AutoSalon()
salon1.add_car("Toyota Camry")

salon2 = AutoSalon()
salon2.add_car("Honda Accord")

# Виведемо список автомобілів для кожного автосалону
print("Autosalon 1 cars:", salon1.get_cars())
print("Autosalon 2 cars:", salon2.get_cars())

# Перевіримо, чи це один і той же екземпляр
print(salon1 is salon2)  # Виведе True
