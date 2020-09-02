from django.db import models

# Create your models here.
class movie(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True)
    Name =models.CharField(max_length=200)
    class meta:
        db_table = "movie"

