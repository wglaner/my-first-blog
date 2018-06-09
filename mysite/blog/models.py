from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tytul = models.CharField(max_length=150)
    tekst = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

#metoda ktora pozwala na publikacje
def publish(self):
    self.published_date = timezone.now()
    self.save()
#a tutaj zwraca nam tytuł wpisu
def __str__(self):
    return self.title
