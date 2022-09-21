from django.db import models
from participants.models import participant
from posts.models import elecsa_post
from django.contrib.auth.models import User

# Create your models here.
class vote(models.Model):
    participant = models.ForeignKey(participant,on_delete=models.CASCADE)
    post = models.ForeignKey(elecsa_post,on_delete=models.CASCADE)
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
