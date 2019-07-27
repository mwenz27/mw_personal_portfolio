from django.db import models


# Create your models here.
class project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.summary[:50] + "..."

