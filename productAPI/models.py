from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Product(models.Model):
    productName = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dateAdded = models.DateField(auto_now_add=True)
    regularPrice = models.FloatField()
    profit = models.FloatField()
    supply = models.IntegerField()
    titleImage = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    image4 = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    slug = models.SlugField()


    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def getTitleImage(self):
        if self.titleImage :
            return 'http://127.0.0.1:8000' + self.titleImage.url 
        else:
            return ''

    def getImage2(self):
        if self.image2 :
            return 'http://127.0.0.1:8000' + self.image2.url 
        else:
            return ''

    def getImage3(self):
        if self.image3 :
            return 'http://127.0.0.1:8000' + self.image3.url 
        else:
            return ''

    def getImage4(self):
        if self.image4 :
            return 'http://127.0.0.1:8000' + self.image4.url 
        else:
            return ''

    def makeThumbnail(self,image, size = (200,200)):
            img = Image.open(image)
            img.convert('RGB')
            img.thumbnail(size)

            thumb_io = BytesIO()
            img.save(thumb_io,'JPEG',quality = 85)

            thumbnail = File(thumb_io, name=image.productName)

            return thumbnail
   
    def thumbnail(self):
        if self.titleImage : 
            self.thumbnail = self.makeThumbnail(self.titleImage)
            self.save()
            return 'http://127.0.0.1:8000' + self.titleImage.url 
        else:
            return ''

    
    