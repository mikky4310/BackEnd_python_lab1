"""Lab2 - Магическая лаборатория зельеварения"""

def transform():
    """Работа с преобразование типов данных"""
    herbs = 5
    crystal_dust = "10"
    magic_essence = "15.5"
    dust_int = int(crystal_dust)
    essence_float = float(magic_essence)
    print("Магическое преобразование ингредиентов:")
    print("Исходные ингредиенты:")
    print(f"Травы: {herbs} штук, тип: {type(herbs)}")
    print(f"Пыль: {crystal_dust}, тип: {type(crystal_dust)}")
    print("Преобразование пыли в магическое число:", dust_int, type(dust_int))
    print("Преобразование эссенции в магическое число:", essence_float, type(essence_float))

def assigning():
    """Работа с присваиваниями"""
    health_potions = 0
    mana_potions = 0
    herbs = 10
    crystal_dust = 15
    print("\nМагическое зельеварение:")
    print(f"Начальные запасы:\nТравы: {herbs}, Пыль: {crystal_dust}")
    print(f"Зелья здоровья:{health_potions}, Зелья маны: {mana_potions}")
    herbs -= 2
    crystal_dust -= 1
    health_potions += 1
    print("После создания зелья здоровья:")
    print(f"Травы: {herbs}, Пыль: {crystal_dust}")
    print(f"Зелья здоровья: {health_potions}")

def conditional_operators():
    """Работа с условными операторами"""
    herbs = 5
    crystal_dust = 3
    print("\nПроверка магических рецептов:")
    print(f"Доступные ингредиенты:\nТравы: {herbs}, Пыль: {crystal_dust}")
    if herbs >= 2 and crystal_dust >= 1:
        print("Можно создать зелье здоровья!")
    else:
        print("Не хватает ингредиентов для зелья здоровья")

    if herbs >= 1 and crystal_dust >= 3:
        print("Можно создать зелье маны!")
    else:
        print("Не хватает ингредиентов для зелья маны")

def potion_brewing():
    """Основная функция и работа с циклами"""
    herbs = 10
    crystal_dust = 15
    health_potions = 0
    mana_potions = 0
    print("\nМагическая лаборатория")
    while herbs > 0 and crystal_dust > 0:
        print(f"\nВаши запасы:\nТравы: {herbs}, Пыль: {crystal_dust}")
        print(f"Ваши зелья:\nЗдоровья: {health_potions}, Маны: {mana_potions}")
        choice = input("Выберите зелье (1 - здоровье, 2 - мана, 0 - выход): ")
        if choice == "0":
            print("Выход из лаборатории...")
            break
        if choice == "1":
            if herbs >= 2 and crystal_dust >= 1:
                herbs -= 2
                crystal_dust -= 1
                health_potions += 1
                print("Зелье здоровья создано!")
            else:
                print("Не хватает ингредиентов для зелья здоровья!")
        elif choice == "2":
            if herbs >= 1 and crystal_dust >= 3:
                herbs -= 1
                crystal_dust -= 3
                mana_potions += 1
                print("Зелье маны создано!")
            else:
                print("Не хватает ингредиентов для зелья маны!")
        else:
            print("Неверный выбор!")

    print("\nИтог:")
    print(f"Создано зелий здоровья: {health_potions}")
    print(f"Создано зелий маны: {mana_potions}")
    print(f"Осталось трав: {herbs}")
    print(f"Осталось пыли: {crystal_dust}")

transform()
assigning()
conditional_operators()
potion_brewing()
