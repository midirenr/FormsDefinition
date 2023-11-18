# Web-приложение для определения заполненных форм.
## Описание:
Web-приложение разработано в рамках тестового задания. Приложение получает запросы с шаблоном формы и возвращает название подходящей формы из базы данных или (если форму найти не удалось) возвращает шаблон с типами полей, которые были сгенерированы на основе типа данных (значений) отправленных в запросе.

## Как запустить:
- Откройте в CMD директорию в которую будете устанавливать проект
- Склонируйте репозиторий командой: ```git clone https://github.com/midirenr/forms_definition.git```

- Создайте виртуальное окружение командой:
1) Для ubuntu/linux: ```sudo python3 -m venv venv```
2) Для windows: ```python -m venv venv```

- Активируйте виртуальное окружение командой:
1) Для ubuntu/linux: ```source venv/bin/activate```
2) Для windows: ```.\venv\Scripts\activate```

- Установите все зависимости из файла requirements.txt: ```pip install -r requirements.txt```

- Запустите локальный сервер Django командой: ```python manage.py runserver```

- Запустите тестовый скрипт (который необходимо было создать по условиям ТЗ) командой: ```python test_script.py```

## Используемые библиотеки (фреймворки):
- [Django Framework](https://www.djangoproject.com/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [tinydb](https://github.com/msiemens/tinydb)
