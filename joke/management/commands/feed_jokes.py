import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from joke.models import Joke
import json


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        blagues_api = os.path.join(
           r'Y:\jokes', 'blagues api'
        )

        for f in os.listdir(blagues_api):
            file_path = os.path.join(blagues_api, f)
            with open(file_path, 'r', encoding='utf-8') as obj:
                data = json.load(obj)
                Joke.objects.bulk_create(
                    [
                        Joke(
                            source='Blagues API',
                            category=element['type'],
                            joke=element['joke'],
                            answer=element['answer']
                        )
                        for element in data
                    ], ignore_conflicts=True
                )
