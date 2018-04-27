import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landingpage.settings')

import django
django.setup()

from faker import Faker
from random import randint, choice

from mainpage.models import User

fake = Faker()

fields = ['.com', '.net', '.mail']

for data in range(25):
    f_name = fake.name()
    f_email = fake.email()

    print(f_name, f_email)
    person = User(name=f_name, email=f_email)
    person.save()


print("Populating complete")
