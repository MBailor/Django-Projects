from django.db import models
from django.db.models import Model

TYPE_CHOICES = [
    ("Title", "title")
]

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default=0)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default=0, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
