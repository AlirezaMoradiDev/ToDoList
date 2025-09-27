from django.db import models
from django.utils.text import slugify
from account.models import MyUser


class Ticket(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()