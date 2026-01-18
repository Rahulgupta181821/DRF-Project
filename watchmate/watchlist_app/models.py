from django.db import models


class StreamPlateform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamPlateform,on_delete=models.CASCADE, related_name="watchlist")
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 










# class Move(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name 