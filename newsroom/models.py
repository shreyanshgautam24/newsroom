from django.db import models

# Create your models here.
class newsdata(models.Model):
    head=models.CharField(max_length=100)
    body=models.TextField(max_length=300)
    def __str__(self):
        return 'Topic: '+str(self.head)
    def snippet(self):
        return self.body[:100]


class City(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    class meta:
        verbose_name_plural='cities'