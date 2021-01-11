from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class ModelMain(models.Model):
    name = models.CharField(max_length=200)
    icon_thumbnail = models.ImageField(upload_to='icon_folder/thumbnail', default='default.png', blank=True)
    icon = models.ImageField(upload_to='menu_images/', default='default.png', blank=True)
    published = models.BooleanField(default=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
