from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    doubt = models.CharField(max_length=5000, default="")
    image = models.ImageField(upload_to="image", default="")


