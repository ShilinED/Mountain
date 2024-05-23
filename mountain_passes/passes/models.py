from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15)

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class PerevalAdded(models.Model):
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    level_winter = models.CharField(max_length=10, blank=True)
    level_summer = models.CharField(max_length=10)
    level_autumn = models.CharField(max_length=10)
    level_spring = models.CharField(max_length=10, blank=True)

class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    data = models.TextField()  # In real scenario, it might be a FileField
