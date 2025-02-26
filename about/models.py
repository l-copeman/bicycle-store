from django.db import models


class About(models.Model):
    """"Order" model"""
    name = models.CharField(max_length=100, blank=True, null=True)
    mission = models.TextField(max_length=1000, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    map_embed = models.TextField(blank=True, null=True, )

    def __str__(self):
        return self.name
