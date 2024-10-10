from django.db import models
from .models import Base_cash_send 


class Operations(Base_cash_send):
    result_of_the_operation = models.CharField(max_length=50)
    status_of_the_operation = models.BooleanField(default=False)
    duration_of_the_operation = models.DurationField(default=0)
    description_of_the_operation = models.TextField(max_length=100)
    user = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE)

    

    class Meta:
            ordering = ['-name_of_country'] 

    def __str__(self):
             return self.name_of_country
