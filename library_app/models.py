from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Job(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])


import uuid


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    job = models.ManyToManyField(Job)

    STATUS = (
        ('r', 'Rabotaet'),
        ('u', 'Uvolen'),
        ('o', 'otpusk'),
    )

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='d')

    class Meta:
        ordering = ["birth_date"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)
