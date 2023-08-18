from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name
    

class WebSeries(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length = 200)
    episodes = models.PositiveIntegerField()
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name = 'watchlist')
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=200, null=True)
    webseries = models.ForeignKey(WebSeries, on_delete=models.CASCADE, related_name='review')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.watch.title + " -- " + str(self.rating)