from django.db import models


# Create your models here.
class DiaryEntry(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=20, default="No Title")
    description = models.CharField(max_length=1000)
    happyness_value = models.IntegerField(default=3)

    def __str__(self):
        return self.title
