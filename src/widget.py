from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    """
    # Разделяем строку на название и номер
    parts = data.rsplit(" ", 1)  # Разделяем строку, сохраняя последний элемент как номер
    if len(parts) != 2:
        raise ValueError("Некорректный формат входных данных. Должен быть тип/название и номер.")

    name, number = parts
    if name.startswith("Счет"):
        # Маскируем номер счета
        masked_number = get_mask_account(number)
    else:
        # Маскируем номер карты
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    """
    try:
        # Парсим дату из строки
        date_obj = datetime.fromisoformat(date_str)
        # Преобразуем в нужный формат
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается строка в формате ISO 8601.")
