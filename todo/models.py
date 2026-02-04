from django.db import models

# Create your models here.

class Todo(models.Model):   
    name = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.name