from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/5.0/topics/db/models/

class LostItem(models.Model):
    lost_loc = models.CharField(max_length = 25)
    lost_latitude = models.IntegerField() # max -> 11
    lost_longetude = models.IntegerField() # max -> 11
    lost_item = models.CharField(max_length = 30)
    item_desc = models.CharField(max_length = 255)
    circle_radio = models.IntegerField(null = True) # max -> 4
    lost_date = models.DateTimeField(auto_now = True)
    lost_fk = models.ForeignKey(User, on_delete = models.CASCADE)
    item_status = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.lost_fk} -> {self.item}"

    def was_found(self):
        return self.item_status

# class FoundItem(models.Model):
#     não deve ter FK da LostItem porque não faz sentido
#     found_latitude = models.IntegerField(max_length = 11)
#     found_longetude = models.IntegerField(max_length = 11)
#     item = models.CharField(max_length = 30)
#     description = models.CharField(max_length = 255)
#     found_date = models.DateTimeField(auto_now = True)
#     found_fk = models.ForeignKey(User, on_delete = models.SET_NULL)

# https://docs.djangoproject.com/en/5.0/topics/migrations/ (django-admin = python manage.py, app_label o app que o models faz parte)

# MIGRATION -> sincronizar/atualizar a base de dados com a models
# makemigration - cria uma nova migration -> django-admin makemigration [<nome_app> [-n <nome_migration>]]
# migrate - aplica a migration -> django-admin migrate [<nome_app> [<nome_migration>]]

# DÚVIDAS:
#    - https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations (2º trecho) -> significa: caso haja uma FK, devo especificar o app da dela?
#    - https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-api-reference (1º trecho) -> "classe abstrata": definição to tipo da classe ou é uma característica?
#    - https://docs.djangoproject.com/en/5.0/topics/db/models/#using-models (3º trecho) -> esse ponto não deveria ser detacado?