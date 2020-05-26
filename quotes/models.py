from django.db import models

class Stock(models.Model):
    # inheritance from models.Model -- django
    # defining columns:
    ticker = models.CharField(max_length=10, )

    # define represntation model - this is for the admin area:
    def __str__(self):
        return self.ticker

