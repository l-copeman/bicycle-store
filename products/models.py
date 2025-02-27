from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Category model"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(
        'Category', blank=False, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=250, unique=True, blank=False, null=False)
    name = models.CharField(
        max_length=250, unique=True, blank=False, null=False)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=3000, blank=False, null=False)
    colour = models.CharField(max_length=30, blank=False, null=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, blank=False, null=False,
        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name
