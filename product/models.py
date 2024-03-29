from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)