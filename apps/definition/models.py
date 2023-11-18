from tinydb import TinyDB

from .utilities.enums import DB_NAME


class DataBase:
    def __init__(self):
        self.db_object = TinyDB(DB_NAME)

    def __del__(self):
        self.db_object.close()

    def get_form_by_example(self, example: dict) -> str or dict:
        """
        Получить имя формы по шаблону

        Описание: функция отравляет запрос в базу данных для получения всех записей, после чего сверяет ключи и значения
        полученные из базы данных с ключами и значениями из шаблона:
        1. В случае, если форма (или формы) из базы данных соответствует(ют) шаблону, возвращает имя той формы, которая
        наиболее подходит под шаблон. Наиболее подходящей формой считается та, у которой наименьшее число лишних полей.
        2. В случае, если подходящую форму найти не удалось, возвращает шаблон.

        :param example: шаблон по которому нужно получить форму
        :return: имя шаблона или сам шаблон
        """
        all_notes = self.db_object.all()
        valid_notes = []

        for note in all_notes:
            if all(field_type in list(note.values()) for field_type in list(example.values())) and \
                    all(field_name in list(note.keys()) for field_name in list(example.keys())):
                valid_notes.append(note)

        if len(valid_notes) == 0:
            return example
        else:
            note = min(valid_notes, key=lambda valid_note: len(valid_note))
            return note['name']
