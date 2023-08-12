from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.CharField(max_length=30)
    date = models.DateField(null=False)

    def __str__(self): 
        return self.title + " by " + self.author + " | postado dia " + str(self.date)
    
