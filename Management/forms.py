from django import forms
from .models import Management_Post


#Creating a form
class ClientCreateForm(forms.ModelForm):
   class Meta:
     model = Management_Post
     fields = "__all__"     
     