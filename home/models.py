from django.db import models

class CustomManager(models.Manager):
    def filter_age(self):
        return super().get_queryset().filter(age__gt=20).filter(self.age % 3 == 0)

class Information(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    github = models.URLField()
    instagram = models.URLField()
    channel_telegram = models.URLField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    icon = models.ImageField(upload_to='information', null=True, blank=True)




