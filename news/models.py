from django.db import models

# Create your models here.
#Editor model this will contain data of our editor
class Editor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
