from django.db import models

# https://docs.djangoproject.com/en/5.0/topics/db/models/

class LostUser(models.Model): #coords, item, desc, contact
    coords = models.CharField(max_length = 11)
    item = models.CharField(max_length = 1)
    description = models.CharField(max_length = 1)
    contact = models.CharField(max_length = 11)
    circle_radio = models.CharField(max_length = 11)
    lost_date = models.DateTimeField(auto_now = True)

# https://docs.djangoproject.com/en/5.0/topics/migrations/ (django-admin = python manage.py, app_label o app que o models faz parte)

# MIGRATION -> sincronizar/atualizar a base de dados com a models
# makemigration - cria uma nova migration -> django-admin makemigration [<nome_app> [-n <nome_migration>]]
# migrate - aplica a migration -> django-admin migrate [<nome_app> [<nome_migration>]]

# DÚVIDAS:
#    - https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations (2º trecho) -> significa: caso haja uma FK, devo especificar o app da dela?
#    - https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-api-reference (1º trecho) -> "classe abstrata": definição to tipo da classe ou é uma característica?
#    - https://docs.djangoproject.com/en/5.0/topics/db/models/#using-models (3º trecho) -> esse ponto não deveria ser detacado?