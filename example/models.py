from django.db import models

class FootballClub(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    is_top_elite = models.BooleanField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Football Clubs'

class Player(models.Model): # new
    name = models.CharField(max_length=100) # new
    age = models.PositiveIntegerField() # new
    club = models.ForeignKey(FootballClub, on_delete=models.CASCADE) # new

    def __str__(self): # new
        return self.name # new

    class Meta: # new
        verbose_name_plural = 'Players' # new
