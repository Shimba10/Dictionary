from django.db import models

# Create your models here.
class Dictionary(models.Model):
    search = models.CharField(max_length=50)

    class Meta:
        db_table = 'Dictionary'

    def __str__(self):
        return self.search
        

