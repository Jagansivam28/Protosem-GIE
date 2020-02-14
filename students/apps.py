from django.apps import AppConfig
from students.task import start

class StudentsConfig(AppConfig):
    name = 'students'

    def ready(self):
       start()
