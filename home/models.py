from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    github = models.URLField()
    instagram = models.URLField()
    channel_telegram = models.URLField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    icon = models.ImageField(upload_to='information', null=True, blank=True)




