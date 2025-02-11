from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Task(models.Model):
    level_priority = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    ]

    status = [
        ('Not completed', 'NOT COMPLETED'),
        ('completed', 'COMPLETED')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    priority = models.CharField(max_length=15, choices=level_priority)
    status = models.CharField(max_length=30, choices=status, default='Not completed')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    view = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def __str__(self):
        return self.title

