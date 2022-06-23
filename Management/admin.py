from django.contrib import admin
from .models import Management_Post
from .forms import ClientCreateForm 


class ClientCreateAdmin(admin.ModelAdmin):
   list_display = ['room_number', 'amount_paid','occupant_name', 'occupant_occupation']
   form = ClientCreateForm
   list_filter = ['room_number']
   search_fields = ['room_number', 'occupant_name']

# Register your models here.
admin.site.register(Management_Post, ClientCreateAdmin)
