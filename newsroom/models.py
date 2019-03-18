from django.db import models

# Create your models here.
class newsdata(models.Model):
    head=models.CharField(max_length=60)
    body=models.TextField(max_length=200)
    def __str__(self):
        return 'news: 1'+str(self.head)
