#!/usr/bin/env python
#Bilgehan Kalay start_date 17/07/2022

"""Django's command-line utility for administrative tasks."""
from msilib.schema import Error
import os
import sys


def checkSecretKey():
    key_list = ['SECRET_KEY', 'GOOGLE_KEY', 'PLACE_ID']
    #check Health.SECRETS file
    if not os.path.isfile('Health/SECRETS.py'):
        #create Health.SECRETS file
        with open('Health/SECRETS.py', 'w') as f:
            for key in key_list:
                f.write(f'{key} = "SET_KEY"\n')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Health.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

  
if __name__ == '__main__':
    checkSecretKey()
    main()


