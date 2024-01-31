from django.db import models

class book(models.Model):
    title=models.CharField(max_length=20)
    auther=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return self.title
