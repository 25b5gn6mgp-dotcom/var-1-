"""
Вариант 2. Конвертер единиц измерения
Практическая работа 1

Программа предлагает пользователю выбрать тип преобразования единиц,
запрашивает значение и выводит результат конвертации.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Перевод градусов Цельсия в градусы Фаренгейта."""
    return celsius * 9 / 5 + 32


def kilometers_to_miles(km: float) -> float:
    """Перевод километров в мили (1 км ≈ 0.621371 мили)."""
    return km * 0.621371


def kilograms_to_pounds(kg: float) -> float:
    """Перевод килограммов в фунты (1 кг ≈ 2.20462 фунта)."""
    return kg * 2.20462


def meters_to_feet(meters: float) -> float:
    """Перевод метров в футы (1 м ≈ 3.28084 фута)."""
    return meters * 3.28084


def get_positive_number(prompt: str) -> float:
    """
    Безопасный ввод положительного числа.
    Повторяет запрос при некорректном вводе.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Ошибка: значение не может быть отрицательным.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное число.")


def main() -> None:
    """Основная функция программы."""
    print("=== Конвертер единиц измерения ===\n")

    # Меню выбора преобразования
    print("Выберите конвертер:")
    print("1. Градус Цельсия -> Градус Фаренгейта")
    print("2. Километры -> Мили")
    print("3. Килограммы -> Фунты")
    print("4. Метры -> Футы")

    # Запрос выбора пользователя
    while True:
        choice = input("\nВаш выбор: ").strip()
        if choice in ("1", "2", "3", "4"):
            break
        else:
            # Обработка неизвестного номера преобразования
            print("Ошибка: неизвестный номер преобразования. Введите число от 1 до 4.")

    # В зависимости от выбора запрашиваем значение и выполняем конвертацию
    if choice == "1":
        value = get_positive_number("Введите температуру (°C): ")
        result = celsius_to_fahrenheit(value)
        print(f"\n{value} C = {result:.1f} F")

    elif choice == "2":
        value = get_positive_number("Введите расстояние (км): ")
        result = kilometers_to_miles(value)
        print(f"\n{value} км = {result:.2f} миль")

    elif choice == "3":
        value = get_positive_number("Введите массу (кг): ")
        result = kilograms_to_pounds(value)
        print(f"\n{value} кг = {result:.2f} фунтов")

    elif choice == "4":
        value = get_positive_number("Введите длину (м): ")
        result = meters_to_feet(value)
        print(f"\n{value} м = {result:.2f} футов")


if __name__ == "__main__":
    main()
