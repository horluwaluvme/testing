from django.db import models

# Create your models here.

class Management_Post(models.Model):
    room_number = models.IntegerField()
    amount_paid = models.CharField(max_length=200)
    occupant_name = models.CharField(max_length=200)
    occupant_email= models.EmailField()
    occupant_occupation = models.CharField(max_length=200)
    number_of_night = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.occupant_name + ' ' + self.occupant_occupation