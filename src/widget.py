from src.masks import get_mask_card_number, get_mask_account


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
