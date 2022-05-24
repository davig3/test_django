from django.db import models

# Create your models here.
# The Tarea class inherits from the models.Model class, which is a class that comes from the
# django.db.models module. 
# 
# The Tarea class has one attribute, tarea, which is a CharField. 
# 
# A CharField is a type of database field that can store text. 
# 
# The max_length parameter specifies the maximum length of the text that can be stored in the field. 
# 
# The __str__ method is a special method that is used to return a string representation of an object. 
# 
# In this case, the string representation of a Tarea object is the text that is stored in the tarea
# attribute. 
# 
# The __str__ method is used by Django to display the object in the admin site.

class Tarea(models.Model):
    tarea = models.CharField(max_length=100)

    def __str__(self):
        return self.tarea