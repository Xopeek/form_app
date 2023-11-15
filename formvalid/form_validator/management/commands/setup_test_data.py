from django.core.management.base import BaseCommand

from form_validator.db_utils import save_template_to_db


class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating the database with test data...')
        self.populate_db_with_test_data()
        self.stdout.write(self.style.SUCCESS(
            'Database populated with test data'
        ))

    def populate_db_with_test_data(self):
        save_template_to_db(
            {
                "name": "User Registration Form",
                "user_email": "email",
                "full_name": "text"
            }
        )
        save_template_to_db(
            {
                "name": "Order Form",
                "customer_email": "email",
                "delivery_date": "date"
            }
        )
        save_template_to_db(
            {
                "name": "Feedback Form",
                "feedback_date": "date",
                "feedback_text": "text",
                "contact_phone": "phone"
            }
        )
