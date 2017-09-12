from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Wanderer(models.Model):



    name = models.CharField(max_length=20,help_text="What's your nickname/title?")
    comment = models.TextField(max_length=200, help_text="A quote that resonates with your character")
    wanderer_status = (('h','Hero of Xeek'),('l','Loser of the Land'))
    #status is determined by whether or not the mission was successful
    status = models.CharField(max_length=1, choices=wanderer_status, default='l')
    guide = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    class Meta:
        ordering = ["name","status","comment"]


    def __str__(self):
        return self.name