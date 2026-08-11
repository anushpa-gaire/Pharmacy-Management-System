from django.db import models

# Create your models here.

class District(models.Model):
    district_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=20)


class Pharmacy(models.Model):
    name = models.CharField(max_length=50, verbose_name="Pharmacy Name")
    registration_number = models.PositiveIntegerField(unique=True, verbose_name="Registration Number")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email Address")
    phone = models.PositiveBigIntegerField(verbose_name="Phone Number")
    website = models.URLField(max_length=100, null=True, blank=True, verbose_name="Website")
    address = models.CharField(max_length=50, verbose_name="Address")
    city = models.CharField(max_length=50, verbose_name="City")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    opening_time = models.TimeField(verbose_name="Opening Time")
    closing_time = models.TimeField(verbose_name="Closing Time")
    status = models.BooleanField(default=False)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = "pharmacy"