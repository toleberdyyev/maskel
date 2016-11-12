from django.db import models
from django.utils import timezone
# Create your models here.

class OrderList(models.Model):
    author = models.ForeignKey('auth.user')
    # author_id =models.ForeignKey('auth÷')
    title = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateField();
