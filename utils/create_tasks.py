import os
import django
from pathlib import Path
import sys
from datetime import datetime

ABSOLUTE_PATH = Path(__file__).parent.parent
sys.path.append(str(ABSOLUTE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
OBJECTS_NUMBER = 100

django.setup()

if __name__ == '__main__':
    from faker import Faker
    from faker.providers import lorem
    from account.models import User
    from task.models import Task

    fake = Faker()
    fake.add_provider(lorem)

    user = User.objects.all().first()

    for i in range(0, OBJECTS_NUMBER):
        Task.objects.create(
            user=user,
            title=fake.text(max_nb_chars=20),
            task_text=fake.text(max_nb_chars=200),
            end_in=datetime.now(),
            status='pendente',
        )
