import re
from django.db import models
from django_mysql.models import ListCharField
from django.utils import timezone

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()

    def __str__(self):
        return self.song_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.uploaded_time = timezone.now()
        else:
            self.uploaded_time = timezone.now()
        super().save(*args, **kwargs)

class Podcast(models.Model):
    podcast_name = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()
    host = models.CharField(max_length=100)
    participants = ListCharField(base_field=models.CharField(max_length=100, blank=True), size=10, max_length=(10*101))

    def __str__(self):
        return self.podcast_name

    @property
    def participants_count(self):
        return len(self.participants)
    
    def save(self, *args, **kwargs):
        """making sure uploaded time is latest, and participants is a list
        as ListField requires a list to be passed before saving to db"""
        part = self.participants
        if not self.id:
            self.participants = re.findall("[\w]+",part)
            self.uploaded_time = timezone.now()
            
        else:
            self.participants = re.findall("[\w]+",part)
            self.uploaded_time = timezone.now()
        super().save(*args, **kwargs)

class AudioBook(models.Model):
    audiobook_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()

    def __str__(self):
        return self.audiobook_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.uploaded_time = timezone.now()
        else:
            self.uploaded_time = timezone.now()
        super().save(*args, **kwargs)