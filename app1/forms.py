from django import  forms
from app1 import  models

class PostForm(forms.ModelForm):

    #le decimos a django que modelo debe usar para cear este formulario
    class Meta:
        model=models.Post
        fields=('titulo','text0',)

