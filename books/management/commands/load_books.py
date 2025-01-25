from csv import DictReader
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load books from CSV file'

    def handle(self, *args, **kwargs):
        with open('data/books.csv', 'r') as file:
            reader = DictReader(file)
            for row in reader:
                Book.objects.get_or_create(
                    libthing_id=row['libthing_id'],
                    defaults={
                        'title': row['title'],
                        'last_name': row['last_name'].strip(),
                        'first_name': row['first_name'].strip(),
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded books')) 