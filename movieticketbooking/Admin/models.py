from django.db import models

class admin(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True)
    Email_ID = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    class meta:
        db_table = "Admin"