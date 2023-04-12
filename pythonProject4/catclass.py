from cat import Cat

# Пример создания объекта Cat с параметрами
cat1 = Cat("Барон", "Мальчик", 2)
cat2 = Cat("Гоша", "Мальчик", 1)
cat3 = Cat("Мухтар", "Мальчик", 0)
cat4 = Cat("Сэм", "Мальчик", 2)

# Вывод параметров каждого объекта
print(f"{cat1.name}, {cat1.gender}, {cat1.age} года")
print(f"{cat2.name}, {cat2.gender}, {cat2.age} год")
print(f"{cat3.name}, {cat3.gender}, {cat3.age} лет")
print(f"{cat4.name}, {cat4.gender}, {cat4.age} года")