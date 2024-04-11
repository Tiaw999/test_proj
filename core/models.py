#######################################################
# Apps
# Tia Walker
# 04-04-24
#######################################################

from django.db import models

# Create your models here.

class Exhibit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField()
    home_sugg = models.TextField()
    outdoor_sugg = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Play(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Data(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    plays_seen = models.ManyToManyField(Play)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exhibit.name


class Media(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name