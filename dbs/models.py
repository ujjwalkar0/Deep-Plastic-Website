from typing import OrderedDict
from django.db import models
from django.contrib.auth.models import User

import datetime

class DailyStatistics(models.Model):
    date = models.DateField(max_length=20)
    location = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    class Meta:
        unique_together = ('location', 'date')
        ordering = ('date','location')

    def __str__(self):
        return f"{self.date} -- {self.location} -- {self.count}"

class UploadImageTest(models.Model):
    image = models.ImageField(upload_to="Images/", blank=True, null=True)
    location = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    
    def save(self, *args, **kwargs):
        try:
            day = DailyStatistics.objects.get(date=self.date, location = self.location)
            day.count+=1
        except DailyStatistics.DoesNotExist:
            day = DailyStatistics.objects.create(date=self.date, location = self.location)
            day.location = self.location
        day.save()
        super(UploadImageTest, self).save(*args, **kwargs)

class Videos(models.Model):
    Upload_File=models.FileField(upload_to='file2link/')