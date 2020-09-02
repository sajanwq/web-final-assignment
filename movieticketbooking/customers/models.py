from django.db import models

class customer(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True)
    Email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    class meta:
        db_table = "customer"


