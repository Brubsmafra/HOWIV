from django.forms import ModelForm
from blog.models import Assist

class AssistForm(ModelForm):
    class Meta:
        model=Assist
        fields= ["nome", "cpf", "telefone", "email", "endereco"]