from django.db import models


# Create your models here.

class Hotel(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300, blank=True, null=True)
    featured_image = models.ImageField()
    rating = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    address = models.CharField(max_length=150)
    miles_from_center = models.IntegerField(default=0)
    starting_price = models.IntegerField(default=0)
    max_guests = models.IntegerField(default=0)
    host_email = models.CharField(max_length=150)
    host_phone = models.CharField(max_length=150)
    breakfast_included = models.BooleanField(default=False)
    prepayment = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.title


class HotelImage(models.Model):
    hotel = models.ForeignKey(
        'Hotel', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
