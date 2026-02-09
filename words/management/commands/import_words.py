import json
import os
from django.core.management.base import BaseCommand
from words.models import Word

class Command(BaseCommand):
    help = 'Import words from words.json'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        json_path = os.path.join(base_dir, 'data', 'words.json')

        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)

        created = 0

        for item in data:
            print(item)
            Word.objects.get_or_create(
                turkish_word=item['turkish_word'],
                english_word=item['english_word'],
                defaults={
                    'level': item['level'],
                    'example_sentence': item['example_sentence']
                }
            )
            created += 1

        self.stdout.write(
            self.style.SUCCESS(f'{created} kelime başarıyla eklendi.')
        )
