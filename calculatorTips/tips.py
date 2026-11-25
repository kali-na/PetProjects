import random
from datetime import datetime
from pathlib import Path

RESTAURANT = "Ресторан на Лавке"
WAITERS = ["Денис", "Оля", "Александра"]
TIP_PERCENTS = (10, 15, 20, 25)
TIPS_FILE = Path(__file__).with_name("tips.txt")  # файл лежит рядом со скриптом


# ---------- Вспомогательные функции ввода ----------

def ask_choice(prompt, valid):
    """Спрашивает число, пока не будет введён один из допустимых вариантов."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) in valid:
            return int(text)
        print(f"Ошибка: выберите один из вариантов {min(valid)}–{max(valid)}.")


def ask_amount(prompt):
    """Спрашивает положительную сумму (допускает запятую и копейки)."""
    while True:
        text = input(prompt).strip().replace(",", ".")
        try:
            amount = round(float(text), 2)
        except ValueError:
            print("Ошибка: введите число, например 500 или 350.50.")
            continue
        if amount <= 0:
            print("Ошибка: сумма должна быть больше нуля.")
            continue
        return amount


def ask_card_number():
    """Спрашивает номер карты: ровно 16 цифр (пробелы игнорируются)."""
    while True:
        number = input("Введите номер карты (16 цифр): ").replace(" ", "")
        if number.isdigit() and len(number) == 16:
            return number
        print("Ошибка: номер карты должен состоять из 16 цифр.")


def fake_card_number():
    """Генерирует номер карты для перевода по СБП (демо)."""
    return "-".join(str(random.randint(5000, 5999)) for _ in range(4))


# ---------- Сохранение в файл ----------

def save_tip(waiter, table, check, tip, method, comment):
    """Дописывает информацию о чаевых в конец txt-файла."""
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    record = (
        f"Дата и время: {now}\n"
        f"Ресторан: {RESTAURANT}\n"
        f"Официант: {waiter}\n"
        f"Стол: {table}\n"
        f"Сумма чека: {check} руб.\n"
        f"Чаевые: {tip:.2f} руб.\n"
        f"Способ оплаты: {method}\n"
        f"Комментарий: {comment or '—'}\n"
        f"{'-' * 40}\n"
    )
    try:
        with open(TIPS_FILE, "a", encoding="utf-8") as file:
            file.write(record)
    except OSError as error:
        print(f"Не удалось сохранить данные в файл: {error}")
    else:
        print(f"Данные сохранены в файл: {TIPS_FILE.name}")


# ---------- Оплата ----------

def pay(amount):
    """
    Единый сценарий оплаты для любой суммы.
    Возвращает название способа оплаты, если оплата прошла,
    и None, если пользователь вернулся назад.
    """
    print("\nКак вы хотите оплатить?")
    print("1. СБП")
    print("2. Карта")
    print("3. Назад")
    method = ask_choice("Выберите цифру: ", {1, 2, 3})

    if method == 3:
        return None

    if method == 1:
        method_name = "СБП"
        print(f"Номер карты для перевода: {fake_card_number()}")
    else:
        method_name = "Карта"
        ask_card_number()  # номер карты в файл не записываем

    print(f"Сумма чаевых: {amount:.2f} руб.")
    print("1. Оплатить")
    print("2. Назад")
    if ask_choice("Выберите цифру: ", {1, 2}) == 2:
        return None

    print("Транзакция успешно проведена.")
    return method_name


# ---------- Основная программа ----------

def main():
    waiter = random.choice(WAITERS)
    table = random.randint(1, 10)
    check = random.randint(2500, 15000)

    print(f'Чаевые: "{RESTAURANT}"')
    print(f"Сумма вашего чека: {check} руб.")
    print(f"Номер стола: {table}")
    print(f"Ваш официант: {waiter}")

    comment = input("Расскажите, всё ли вам понравилось?: ").strip()
    print("Спасибо за отзыв!")

    other_option = len(TIP_PERCENTS) + 1
    exit_option = len(TIP_PERCENTS) + 2

    while True:
        print(f"\nСколько вы хотите оставить чаевых официанту {waiter}?")
        for number, percent in enumerate(TIP_PERCENTS, start=1):
            print(f"{number}. {percent}% от суммы чека: {check * percent / 100:.2f} руб.")
        print(f"{other_option}. Другая сумма")
        print(f"{exit_option}. Выйти")

        choice = ask_choice("Выберите пункт: ", set(range(1, exit_option + 1)))

        if choice == exit_option:
            print("Всего доброго!")
            break

        if choice == other_option:
            amount = ask_amount("Введите сумму чаевых: ")
        else:
            amount = round(check * TIP_PERCENTS[choice - 1] / 100, 2)

        method_name = pay(amount)
        if method_name:
            save_tip(waiter, table, check, amount, method_name, comment)
            print("Спасибо! Всего доброго.")
            break


if __name__ == "__main__":
    main()
