from django.db import models

# Create your models here.
class myDatabase(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+" , "+str(self.number)
