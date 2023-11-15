import json

from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Perform test requests to the Django server'

    def handle(self, *args, **options):
        url = 'http://127.0.0.1:8000/get_form/'  # Замените на ваш адрес

        # Тестовые данные (поля формы и их значения)
        test_data_list = [
            {
                "user_email": "test@example.com",
                "full_name": "John Doe",
            },
            {
                "delivery_date": "2022-12-01",
                "customer_email": "test@example.com",
            },
            {
                "feedback_date": "2022-11-15",
                "feedback_text": "text",
                "contact_phone": "+71234567890",
            },
            {
                "user_email": "text",
                "full_name": "+71234567890",
            },
            {
                "delivery_date": "2022-12-01",
                "customer_email": "2022-12-01",
            },
        ]

        for test_data in test_data_list:
            response = requests.post(url, data=test_data)

            try:
                response_json = response.json()
                # Печать ответа сервера
                self.stdout.write(json.dumps(response_json, indent=2))
            except json.JSONDecodeError:
                self.stdout.write(response.text)
