from django.db import models


# Create your models here.
class DiaryEntry(models.Model):
    pub_date = models.DateTimeField("date published")
    description = models.CharField(max_length=1000)
    happyness_value = models.IntegerField(default=3)
