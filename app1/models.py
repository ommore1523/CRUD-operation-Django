

# Create your models here.


# import the standard Django Model
# from built-in library
from django.db import models
import datetime

# declare a new model with a name "GeeksModel"
class TaskModel(models.Model):
    # fields of the model
    datetime= models.DateTimeField(default=datetime.datetime.now())
    task = models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.task

