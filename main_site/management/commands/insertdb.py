from django.core.management.base import BaseCommand, CommandError
import csv
from main_site.models import StudentModel

class Command(BaseCommand):
    help = 'Import data to the database from external file [CSV files]'


    # arguments :

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help='Provide target files file path')
        parser.add_argument("--upload_to_db", type=str, action='append', help='save all data to the database.')
        


    def handle(self, *args, **options):

        data_set = options["file_path"]
        upload_to_db = options["upload_to_db"]

        

        try:
            with open(data_set, 'r') as file:
                csv_data = csv.DictReader(file)
                # upload through the 'Student' model to the database
                if options['upload_to_db']:
                    for data in csv_data:
                        StudentModel.objects.create(**data)
                    self.stdout.write(self.style.SUCCESS("Data Successfully Imported !!! "))
                
                else:
                # if '--upload_to_bd' argument is empty , this piece code only show sample of data without 
                # importing data into the database
                    data_count = 0
                    print('Preview of data :')
                    for data in csv_data:
                        data_count += 1
                        if data_count <= 10 :
                            print(data)
                    self.stdout.write(self.style.WARNING("Data not imported into the database. "))
        except:
                return CommandError('file does not exists !!!')
            
    
                
        
        
 


# example how to use it :
# py manage.py insertdb "C:\Users\Desktop\Projects\Datasets\student_data.csv" --upload_to_db upload_to_db






