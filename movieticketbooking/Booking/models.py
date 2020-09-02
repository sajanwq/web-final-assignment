from django.db import models

class booking(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True)
    Customer_Name = models.CharField(max_length=200)
    Email_ID = models.CharField(max_length=200)
    Tickets = models.CharField(max_length=200)
    Seat_Type = models.CharField(max_length=200)
    Theatre = models.CharField(max_length=200)
    Movies = models.CharField(max_length=200)


    class meta:
        db_table = "booking"

