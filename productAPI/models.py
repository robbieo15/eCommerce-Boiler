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
    titleImage = models.ImageField(upload_to = 'uploads', default="default.png", blank=True, null=True)
    image2 = models.ImageField(upload_to = 'uploads', default="default.png", blank=True, null=True)
    image3 = models.ImageField(upload_to = 'uploads', default="default.png", blank=True, null=True)
    image4 = models.ImageField(upload_to = 'uploads', default="default.png", blank=True, null=True)
    slug = models.SlugField(upload_to = 'uploads', default="default.png", blank=True, null=True)


    def __str__(self):
        return self.productName
    