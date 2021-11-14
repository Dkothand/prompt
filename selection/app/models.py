from django.db import models


# Create your models here.
class Provider(models.Model):

    class EaseOfUse(models.IntegerChoices):
        HARDEST = 1
        HARD = 2
        AVERAGE = 3
        EASY = 4
        EASIEST = 5

    name = models.CharField(max_length=124, blank=False, default='')
    fees = models.DecimalField(max_digits=19, decimal_places=4)
    minimum_balance = models.DecimalField(max_digits=19, decimal_places=4)
    automated = models.BooleanField(default=False, verbose_name="Automated or Self-Directed")
    advisor = models.BooleanField(default=False, verbose_name="Human Advisor Available")
    ease_of_use = models.IntegerField(choices=EaseOfUse.choices, default=EaseOfUse.AVERAGE)
