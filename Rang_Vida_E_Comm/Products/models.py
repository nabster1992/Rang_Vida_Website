from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    #models.Model is a base class provided by Django, and it includes all the necessary functionalities to interact with a database. When you inherit from models.Model, your class becomes a Django model, and you gain access to features like database querying, field types 
    
    #In Django, a SlugField is a field used to store a short label or identifier for a model instance in a way that is suitable for use in URLs. It's often used to create human-readable and SEO-friendly URLs.

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
        #the class Meta is a class container within a model class that allows you to specify various options and metadata for the model. It's a way to provide additional information about the behavior of the model, beyond the definition of fields.

    def __str__(self):
        return self.name
    #In the Django admin interface or when you print an instance of YourModel, it will display the value of the name field, making it easier for humans to identify and understand the instances of the model.

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #this connects the product database model to the category model
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        
        ordering = ('-created_at',)
        #minus means descending order

    def __str__(self):
        return self.name
    
   #the purpose for this is to show price in dollars and cents, since we are in pkr we dont need this? maybe?
    def get_display_price(self):
        return self.price / 100
    

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            
            else:
                return 'https://via.placeholder.com/600x600.jpg'
            
            # return self.thumbnail.url: If a thumbnail exists, returns its URL.
# if self.image:: If no thumbnail exists, checks if the instance has an image.
# self.thumbnail = self.make_thumbnail(self.image): Generates a thumbnail using the make_thumbnail method and assigns it to the instance's thumbnail field.
# self.save(): Saves the instance to persist the newly generated thumbnail.
# return self.thumbnail.url: Returns the URL of the generated thumbnail.
# else: (for the outer else): If neither a thumbnail nor an image is present, returns a placeholder URL.




            
    def make_thumbnail(self, image, size=(640, 640)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        else:
            return 0
    
#     def make_thumbnail(self, image, size=(300, 300)):: Method signature with parameters self (assumed to be a Django model instance), image (the original image), and an optional size parameter (defaulting to (300, 300)).
# img = image.open(image): Opens the original image using the open method provided by the ImageField.
# img.convert('RGB'): Converts the image to the RGB color mode.
# img.thumbnail(size): Generates a thumbnail of the specified size.
# thumb_io = BytesIO(): Creates a BytesIO object to store the thumbnail image.
# img.save(thumb_io, 'JPEG', quality=85): Saves the thumbnail image to the BytesIO object as a JPEG image with a quality of 85.
# thumbnail = File(thumb_io, name=image.name): Creates a Django File object from the BytesIO object, using the original image's name.
# return thumbnail: Returns the generated thumbnail as a Django File object.
    

class Review(models.Model):   
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    content= models.CharField(max_length=255)
    rating = models.IntegerField(default=3)
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ('-created_at',)

    
            





    

    
   


