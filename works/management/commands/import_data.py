from argparse import FileType
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Name of the file to be imported')
    
    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(file_name, 'r') as file:
            works = csv.DictReader(file)

            for line in works:
                print(line)