from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

class Command(BaseCommand):
    help = 'Import data to the database from external file [CSV files]'


    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help='Provide target files file path')
        parser.add_argument("--model_name", type=str, help='provide model name to import data')
        


    def handle(self, *args, **options):

        data_set = options["file_path"]
        selected_model = options["model_name"].capitalize()

        model = None

        for app_config in apps.get_app_configs():

            try:
                model = apps.get_model(app_config.label, selected_model)
                break

            except LookupError:
                continue

        if not model:
            raise CommandError(f'model {model} not found in any apps !! ')
        
        else:
            with open(data_set, 'r') as file:
                csv_data = csv.DictReader(file)
                for data in csv_data:
                    model.objects.create(**data)

            self.stdout.write(self.style.SUCCESS("Data Successfully Imported !!! "))

    
                
        
        
 
# example how to use it :
# py manage.py advance_insert "C:\Users\Desktop\Datasets\customer_demo_records.csv" --model_name CustomerID





