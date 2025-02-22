from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

# https://docs.djangoproject.com/en/5.0/topics/forms/media/#assets-as-a-static-definition

class CreateAccount(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "last_name", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels_text = ["Nome de usuário", "Seu nome", "Email", "Senha", "Confirmar senha"]
        
        for (text, field) in zip(labels_text, self.fields):
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"class": "field", "id": field})
            self.fields[field].label = text