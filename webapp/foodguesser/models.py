from django.db import models

# Create your models here.i
class Food(models.Model):
    image = models.ImageField()
    calories = models.IntegerField()

    def __str__(self):
        return str(self.image)

class Score(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()
    guess_count = models.IntegerField()

    def __str__(self):
        return self.username + ": " + str(score) + " away over " + str(guess_count) + " guesses."
