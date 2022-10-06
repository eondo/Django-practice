from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=200)
    issue_b = models.CharField(max_length=200)


class Comment(models.Model):
    # choice 옵션에 지정할 값
    COLOR_CHOICES = (
        ('BLUE', 'BLUE'),
        ('RED', 'RED')
    )
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    pick = models.CharField(max_length=200, choices=COLOR_CHOICES)
    content = models.CharField(max_length=200)