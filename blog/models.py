from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    SUBJECT_CHOICES = (
        ('aj','Anglický jazyk'),
        ('b','Biologie'),
        ('cj','Český jazyk a literatura'),
        ('j','Jazyky'),
        ('f','Fyzika'),
        ('ch','Chemie'),
        ('m','Matematika'),
        ('sv','Společenské vědy'),
        ('z','Zeměpis'),
        ('vp','Volitelné předměty'),
        ('other','Ostatní'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES,null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
