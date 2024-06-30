from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    parent = models.ForeignKey(Person, related_name='children', on_delete=models.CASCADE)
    child = models.ForeignKey(Person, related_name='parents', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent.name} -> {self.child.name}"
