from django.db import models

class SustainabilityPractice(models.Model):
    description = models.TextField()
    success_story = models.TextField()

class Incentive(models.Model):
    practice = models.ForeignKey(SustainabilityPractice, on_delete=models.CASCADE)
    reward = models.CharField(max_length=100)
    points = models.IntegerField()