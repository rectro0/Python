from django.db import models
from django.utils.timezone import now

# Create your models here.

class Topic(models.Model):
    """the user's topic """
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300 , default="")

    date = models.DateTimeField(auto_now_add=True )



    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic , on_delete=models.CASCADE)
  
    text= models.TextField()
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta :
     verbose_name_plural = 'entries'

     def __str__(self):
        
        return self.text[:50] +'...'







