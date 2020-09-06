from django.db import models


TYPE_PREFIX = [
    ("Mr.", "Mr."),
    ("Mrs.", "Mrs."),
    ("Ms.", "M s."),
    ("Lord", "Lord"),
    ("Lady", "Lady"),
]


class Profiles(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_PREFIX)
    FirstName = models.CharField(max_length=60, default="", blank=True, null=False)
    LastName = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.CharField(max_length=120, default="", blank=True, null=False)
    Username = models.CharField(max_length=100, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.FirstName
