from django.db import models
from posts.models import elecsa_post

class participant(models.Model):
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=250)
    post = models.ForeignKey(elecsa_post,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image",upload_to="static")
    def __str__(self) -> str:
        return self.name