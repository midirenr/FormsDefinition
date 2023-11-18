import re


def get_field_type(field_value: str) -> str:
    """
    Получить тип поля по его значению

    Описание: функция использует регулярные выражения для определения типа входящего поля. Если ни одно из регулярных
    выражений не смогло отследить паттерн, то будет считаться что данное поле имеет тип Text.

    :param field_value: значение поля, тип которого необходимо получить
    :return: тип поля
    """
    # Здесь убираю все "пустые" символы из входной строки для корректной валидации номера телефона при записи
    # с пробелами и без пробелов
    field_value = "".join(field_value.split())
    if re.search(r"((\+7|7)+([0-9]){10})", field_value) is not None:
        return 'phone'

    if re.search(r"[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}", field_value) is not None:
        return 'email'

    if re.search(r"(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d", field_value) is not None:
        return 'date'

    return 'text'
