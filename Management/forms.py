from django import forms
from .models import Management_Post


#Creating a form
class ClientCreateForm(forms.ModelForm):
   class Meta:
     model = Management_Post
     fields = ['room_number', 'amount_paid', 'occupant_name', 'occupant_email', 'occupant_occupation', 'number_of_night', 'start_date', 'end_date']
     
     