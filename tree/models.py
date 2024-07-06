from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class FamilyMember(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    child_number = models.PositiveIntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    spouse = models.ForeignKey('self', null=True, blank=True, related_name='spouse_members', on_delete=models.CASCADE)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)

    def save(self, *args, **kwargs):
        self.name = ' '.join(word.capitalize() for word in self.name.split()) # Capitalize first letter of name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'child_number']