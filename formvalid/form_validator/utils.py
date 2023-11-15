from datetime import datetime
from itertools import combinations

from tinydb import Query


class ValidForm:
    """Валидация полей отправленного запроса.
    Согласно заданию необходимо валидацию производить в следующем порядке:
     1. Дата.
     2. Телефон
     3. Почта
     Непрошедшим валидацию полям  присуждается тип поля 'text'
    """
    def __init__(self, value):
        self.value = value
        self.type_form = self.validate()

    def validate(self):
        if self.is_date():
            return 'date'
        elif self.is_phone():
            return 'phone'
        elif self.is_email():
            return 'email'
        else:
            return 'text'

    def is_date(self):
        date_formats = ['%d.%m.%Y', '%Y-%m-%d']

        for date_format in date_formats:
            try:
                datetime.strptime(self.value, date_format)
                return True
            except ValueError:
                pass
        return False

    def is_phone(self):
        if self.value.startswith('+7'):
            phone_number = ''.join(c for c in self.value[2:] if c.isdigit())
            return len(phone_number) == 10
        return False

    def is_email(self):
        parts = self.value.split('@', maxsplit=1)
        return len(parts) == 2 and '.' in parts[1]


def find_forms(db, request):
    result = []

    if len(request) == 0:
        return result

    for count_field_in_find in range(1, len(request) + 1):
        iter_find = combinations(request.items(), count_field_in_find)
        iter_find = list(map(lambda x: dict(x), iter_find))

        for comb in iter_find:
            # Используем запрос к базе данных TinyDB для поиска документов
            query = Query()
            filtered_docs = db.search(query.fragment(comb))

            # Проверяем,
            # совпадают ли все поля запроса с полями в каждом документе
            for doc in filtered_docs:
                # Если все поля запроса совпадают,
                # добавляем документ в результат
                if all(doc.get(field) == request[field] for field in request):
                    result.append(dict(doc.items()))

    return result
