from django.db import models

class GarminWatch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    fitness_tracking = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    cycling = models.BooleanField(default=False)
    running = models.BooleanField(default=False)
    hiking = models.BooleanField(default=False)
    rugged = models.BooleanField(default=False)
    battery_life = models.IntegerField()

    def __str__(self):
        return self.name
