from django.db import models
from django_countries.fields import CountryField

class About(models.Model):

    Automotive = 'Automotive'
    biz_cat = (
        ("Automotive", 'Automotive'),
        ("Education_Learning", 'Education & Learning'),
        ("Entertainment", 'Entertainment'),
        ("Financial_Services", 'Financial Services'),
        ("Hair_Beauty", 'Hair Beauty'),
        ("Medical", 'Medical'),
         ("Professional_Services", 'Professional Services'),
        ("Restaurants", 'Restaurants'),
        ("Retail_Shopping" , 'Retail Shopping'),
        ("Sports_Recreation", 'Sports Recreation'),
        ("Trades", 'Trades'),
        ("Other", 'Other'),
    )

    name = models.CharField(max_length=300)
    category = models.CharField(
        max_length=100,
        choices=biz_cat,
        default=Automotive,
    )
    description = models.TextField()
    email = models.EmailField(max_length=300)
    phone = models.IntegerField()
    address = models.CharField(max_length=900)
    country = CountryField(blank_label='(select country)')
    profile_pic = models.ImageField(upload_to='images', blank=True, default="/mnt/project/media/images/barcelona.jpg")
    #https://pypi.python.org/pypi/django-countries




    def __str__(self):              # __unicode__ on Python 2
        return self.name



