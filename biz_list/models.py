from django.db import models
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse

class About(models.Model):

    Automotive = 'Automotive'
    biz_cat = (
        ("Automotive", 'Automotive'),
        ("Education_Learning", 'Education & Learning'),
        ("Entertainment", 'Entertainment'),
        ("Financial_Services", 'Financial Services'),
        ("Hair_Beauty", 'Hair Beauty'),
        ("Medical", 'Medical'),
         ("Services", 'Services'),
        ("Restaurants", 'Restaurants'),
        ("Retail_Shopping" , 'Retail Shopping'),
        ("Sports_Recreation", 'Sports Recreation'),
        ("Real_Estate", 'Real Estate'),
        ("Other", 'Others'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=100,
        choices=biz_cat,
        default=Automotive,
    )
    brief_description = models.TextField(max_length=300)
    description = models.TextField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=900)
    city = models.CharField(max_length=900)
    country = CountryField(blank_label='(select country)')
    website = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    pinterest = models.URLField(max_length=200, blank=True)
    snapchat = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    google_plus = models.URLField(max_length=200, blank=True)
    approved_published = models.BooleanField(default=False)

    def approve(self):
        self.approved_published = True
        self.save()

    def get_absolute_url(self):
        return reverse("/drafts/",kwargs={'pk':self.pk})


    #profile_pic = models.ImageField(upload_to='images', blank=True, default="/mnt/project/media/images/barcelona.jpg")
    #https://pypi.python.org/pypi/django-countries

    def __str__(self):              # __unicode__ on Python 2
        return " %s ==> %s " % (self.name, self.approved_published)



