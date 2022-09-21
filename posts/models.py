from django.db import models

# Create your models here.
class elecsa_post(models.Model):
    post_name = models.CharField(max_length=250)
    post_description = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.post_name