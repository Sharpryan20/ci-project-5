from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = CloudinaryField('image', default='placeholder')
    

    def __str__(self):
        return self.name


