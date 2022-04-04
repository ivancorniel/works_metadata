from django.core.management.base import BaseCommand
from works.models import Works
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Name of the file to be imported')
    
    def handle(self, **kwargs):
        file_name = kwargs['file_name']
        
        with open(file_name, 'r') as file:
            works_from_file = csv.DictReader(file)
            cleaned_works = []
        
            for line in works_from_file: 
                contributor = tuple(line['contributors'].split('|'))
                
                if all((line['title'], contributor, line['iswc'])):
                    cleaned_works.append((line['title'], contributor, line['iswc']))
                elif not line['iswc']:
                    line['iswc'] = line['title'] + '-' + str(contributor[0]) 
                    cleaned_works.append((line['title'], contributor, line['iswc']))
                    
            for work in set(cleaned_works):
                try:
                    Works.objects.get_or_create(title=work[0], contributors= work[1], iswc=work[2])
                except:
                    pass
