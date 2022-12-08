from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    productName = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dateAdded = models.DateField()
    regularPrice = models.FloatField()
    profit = models.FloatField()
    supply = models.IntegerField()
    titleImage = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
        
    def __str__(self):
        return self.productName
    