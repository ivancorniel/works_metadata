from django.core.management.base import BaseCommand
import csv

from works.models import Works, Contributor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Name of the file to be imported')
    
    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        
        with open(file_name, 'r') as file:
            works_from_file = csv.DictReader(file)
            cleaned_works = []
            # contributors = []
        
            for line in works_from_file: 

                work_fields = (line['title'], line['iswc'])
                contributor = line['contributors'].split('|')
                
                if all(work_fields):
                        cleaned_works.append(work_fields)
        
                # for contributor in contributor:
                #     print(line['title'], '-', contributor)
        
            for work in set(cleaned_works):
                Works.objects.get_or_create(title=work[0], iswc=work[1])
